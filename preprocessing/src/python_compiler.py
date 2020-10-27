import json
import gzip
import dis
import pathlib
import io
import tqdm


def python_to_bytecode_from_file(
    input_file,
    output_file,
    content="content",
    progress_bar=None,
    filter_file=None,
):
    """
    Reads json objects and converts contents member from python to bytecode.
    """
    for line in input_file:
        json_obj = json.loads(line)
        with io.StringIO() as output_buffer:
            try:
                dis.dis(json_obj[content], file=output_buffer)
                json_obj[content] = output_buffer.getvalue()
                output_file.write(json.dumps(json_obj) + "\n")
                if filter_file is not None:
                    filter_file.write(line)
            except Exception:
                # Most likely syntax error from Python 2
                if filter_file is None:
                    json_obj[content] = None
                    output_file.write(json.dumps(json_obj) + "\n")
                pass

        progress_bar.update(len(line.encode("utf-8")))


def python_to_bytecode(
    input_path,
    output_path,
    content="content",
    progress_bar=True,
    filter_path=None,
):
    if isinstance(input_path, str):
        input_path = pathlib.PurePath(input_path)
    if isinstance(output_path, str):
        output_path = pathlib.PurePath(output_path)
    input_fn = gzip.open if (input_path.suffix == ".gz") else open
    output_fn = gzip.open if (output_path.suffix == ".gz") else open

    if filter_path is not None:
        if isinstance(filter_path, str):
            filter_path = pathlib.PurePath(filter_path)
        filter_fn = gzip.open if (filter_path.suffix == ".gz") else open

    with input_fn(input_path, mode="rt") as input_file:
        with output_fn(output_path, mode="wt") as output_file:
            # use a dummy __enter__, __exit__ if progress_bar is False
            with (
                filter_fn(filter_path, mode="wt")
                if (filter_path is not None)
                else io.StringIO()
            ) as filter_file:
                with (
                    tqdm.tqdm(
                        total=pathlib.Path(input_path).stat().st_size,
                        unit="B",
                        unit_scale=True,
                        unit_divisor=1024,
                    )
                    if progress_bar
                    else io.StringIO()
                ) as pbar:
                    filter_file_to_pass = (
                        filter_file if filter_path is not None else None
                    )
                    pbar_to_pass = pbar if progress_bar else None
                    python_to_bytecode_from_file(
                        input_file,
                        output_file,
                        content=content,
                        progress_bar=pbar_to_pass,
                        filter_file=filter_file_to_pass,
                    )
