import json
import gzip
import pathlib
import io
import tqdm
import warnings
import py_compile
import multiprocessing as mp
import dis
import contextlib
import preprocessing.src.code_tokenizer as code_tokenizer
import preprocessing.src.dis_tokenizer as dis_tokenizer
import sys

# hex_version=50792944 is sys.version_info(major=3, minor=7, micro=9, releaselevel='final', serial=0)
def python_to_dis(python_code, hexversion=50792944):
    assert sys.hexversion == hexversion, "Hex version does not match"
    try:
        with io.StringIO() as output_buffer:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                dis.dis(python_code, file=output_buffer)
            return output_buffer.getvalue()
    except:
        return None


def python_to_dis_line(line, input_content, output_content, filter_none=True, **kwargs):
    json_obj = json.loads(line)
    if input_content in json_obj:
        bytecode = python_to_dis(json_obj[input_content], **kwargs)
    else:
        bytecode = None

    if filter_none and bytecode is None:
        return None

    json_obj[output_content] = bytecode
    return json.dumps(json_obj) + "\n"


def python_to_dis_worker(
    input_queue, output_queue, input_content, output_content, **kwargs
):
    for line in iter(input_queue.get, None):
        output_line = python_to_dis_line(line, input_content, output_content, **kwargs)
        if output_line is not None:
            output_queue.put(output_line)


def python_to_dis_output_worker(output_queue, output_file):
    for line in iter(output_queue.get, None):
        output_file.write(line)


def python_to_dis_dataset_helper(
    input_file,
    output_file,
    input_content="content",
    output_content="bytecode",
    progress_bar=None,
    num_processes=8,
    input_queue_size=1000,
    output_queue_size=1000,
    **kwargs
):
    input_queue = mp.Queue(maxsize=input_queue_size)
    output_queue = mp.Queue(maxsize=output_queue_size)

    workers = []
    writer = mp.Process(
        target=python_to_dis_output_worker, args=(output_queue, output_file)
    )

    try:
        for _ in range(num_processes):
            workers.append(
                mp.Process(
                    target=python_to_dis_worker,
                    args=(input_queue, output_queue, input_content, output_content),
                    kwargs=kwargs,
                )
            )
            workers[-1].start()

        writer.start()

        for line in input_file:
            input_queue.put(line)
            if progress_bar is not None:
                progress_bar.update(len(line.encode()))

    finally:
        for _ in range(num_processes):
            input_queue.put(None)

        for p in workers:
            p.join()

        output_queue.put(None)
        writer.join()


def python_to_dis_dataset(input_path, output_path, progress_bar=True, **kwargs):
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
                python_to_dis_dataset_helper(
                    input_file, output_file, progress_bar=pbar_to_pass, **kwargs
                )


def geeks_python_to_dataset_json(line, filter_none=True, **kwargs):
    """
    Parse and compile the format of the release geeks_for_geeks validation and test set
    """
    name, sep, detok = line.partition("|")
    if sep == "":
        return None

    detok = detok.strip()
    code = code_tokenizer.detokenize_python(detok)
    bytecode = dis_tokenizer.tokenize_dis(python_to_dis(code))
    if bytecode is None:
        return None

    # Handle list comprehensions later
    funcs = dis_tokenizer.extract_functions_dis(bytecode)
    if funcs is None:
        return None

    functions_standalone, functions_class = funcs
    if len(functions_standalone) > 1 or len(functions_class) > 0:
        return None

    result = functions_standalone[0]

    name = name.strip()
    py_line = line.strip()
    dis_line = name + " | " + result
    return json.dumps({"python": py_line, "dis": dis_line}) + "\n"


def code_to_geeks_dataset(line, prefix="VALID_", sep="|", **kwargs):
    """
    Convert from function to the format of the geeks_for_geeks validation set
    """
    line_no = code_to_geeks_dataset.counter
    code_to_geeks_dataset.counter += 1
    return prefix + str(line_no) + " " + sep + " " + line


code_to_geeks_dataset.counter = 0


def strip_ids_dataset(line, sep=" | ", **kwargs):
    _, _, sent = line.partition(sep)

    return sent
