import json
import gzip
import dis
import pathlib
import io
import tqdm


def python_to_bytecode_from_file(
    input_file, output_file, limit=None, content="content", progress_bar=None
):
    """
    Reads json objects and converts contents member from python to bytecode.
    """
    line_count = 0
    for line in input_file:
        if limit is not None and line_count >= limit:
            break
        json_obj = json.loads(line)
        with io.StringIO() as output_buffer:
            try:
                dis.dis(json_obj[content], file=output_buffer)
                json_obj[content] = output_buffer.getvalue()
            except Exception as ex:
                # Most likely syntax error from Python 2
                json_obj[content] = None
        output_file.write(json.dumps(json_obj) + "\n")
        progress_bar.update(len(line.encode("utf-8")))
        line_count += 1


def python_to_bytecode(
    input_path, output_path, limit=None, content="content", progress_bar=True
):
    if isinstance(input_path, str):
        input_path = pathlib.PurePath(input_path)
    if isinstance(output_path, str):
        output_path = pathlib.PurePath(output_path)
    input_fn = gzip.open if (input_path.suffix == ".gz") else open
    output_fn = gzip.open if (output_path.suffix == ".gz") else open
    with input_fn(input_path, mode="rt") as input_file:
        with output_fn(output_path, mode="wt") as output_file:
            # use a dummy __enter__, __exit__ if progress_bar is False
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
                pbar_to_pass = pbar if progress_bar else None
                python_to_bytecode_from_file(
                    input_file,
                    output_file,
                    limit=limit,
                    content=content,
                    progress_bar=pbar_to_pass,
                )

