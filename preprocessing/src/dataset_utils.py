import contextlib
import gzip
import hashlib
import io
import json
import multiprocessing as mp
import pathlib

import tqdm


def shard_dataset_helper(
    input_file, output_files, input_content="content", progress_bar=None, **kwargs
):
    for line in input_file:
        json_obj = json.loads(line)
        content = json_obj[input_content] if input_content in json_obj else ""
        hash_bytes = hashlib.md5(content.encode()).digest()
        index = int.from_bytes(hash_bytes, byteorder="big", signed=False) % len(
            output_files
        )
        output_files[index].write(line)

        if progress_bar is not None:
            progress_bar.update(len(line.encode()))


def shard_dataset(
    input_path, output_path_pattern, shards=8, progress_bar=True, **kwargs
):
    if isinstance(input_path, str):
        input_path = pathlib.PurePath(input_path)
    if isinstance(output_path_pattern, str):
        output_path_pattern = pathlib.PurePath(output_path_pattern)
    input_fn = gzip.open if (input_path.suffix == ".gz") else open
    output_fn = gzip.open if (output_path_pattern.suffix == ".gz") else open

    output_paths = [
        output_path_pattern.with_name(output_path_pattern.name.replace("*", str(i)))
        for i in range(shards)
    ]

    with input_fn(input_path, mode="rt") as input_file:
        with contextlib.ExitStack() as stack:
            output_files = [
                stack.enter_context(output_fn(output_path, mode="wt"))
                for output_path in output_paths
            ]
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
                shard_dataset_helper(
                    input_file, output_files, progress_bar=pbar_to_pass, **kwargs
                )


def map_dataset_unordered_worker(input_queue, output_queue, func, **kwargs):
    for line in iter(input_queue.get, None):
        output_line = func(line, **kwargs)
        if output_line is not None:
            output_queue.put(output_line)


def map_dataset_unordered_output_worker(output_queue, output_file):
    for line in iter(output_queue.get, None):
        output_file.write(line)


def map_dataset_unordered_helper(
    input_file,
    output_file,
    func,
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
        target=map_dataset_unordered_output_worker, args=(output_queue, output_file)
    )

    try:
        for _ in range(num_processes):
            workers.append(
                mp.Process(
                    target=map_dataset_unordered_worker,
                    args=(input_queue, output_queue, func),
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


def map_dataset_unordered(input_path, output_path, func, progress_bar=True, **kwargs):
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
                map_dataset_unordered_helper(
                    input_file, output_file, func, progress_bar=pbar_to_pass, **kwargs
                )


def split_dataset_helper(input_file, output_files, progress_bar=None, **kwargs):
    index = 0
    for line in input_file:
        output_files[index % len(output_files)].write(line)
        if progress_bar is not None:
            progress_bar.update(len(line.encode()))
        index += 1


def split_dataset(
    input_path, output_path_pattern, num_files=2, progress_bar=True, **kwargs
):
    if isinstance(input_path, str):
        input_path = pathlib.PurePath(input_path)
    if isinstance(output_path_pattern, str):
        output_path_pattern = pathlib.PurePath(output_path_pattern)
    input_fn = gzip.open if (input_path.suffix == ".gz") else open
    output_fn = gzip.open if (output_path_pattern.suffix == ".gz") else open

    output_paths = [
        output_path_pattern.with_name(output_path_pattern.name.replace("*", str(i)))
        for i in range(num_files)
    ]

    with input_fn(input_path, mode="rt") as input_file:
        with contextlib.ExitStack() as stack:
            output_files = [
                stack.enter_context(output_fn(output_path, mode="wt"))
                for output_path in output_paths
            ]
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
                split_dataset_helper(
                    input_file, output_files, progress_bar=pbar_to_pass, **kwargs
                )


def select_json_field(
    line,
    input_field="content",
    output_field="content",
    field_set=["content", "bytecode"],
):
    json_obj = json.loads(line)
    if input_field in json_obj:
        json_obj[output_field] = json_obj[input_field]
    for field in field_set:
        if field != output_field:
            del json_obj[field]

    return json.dumps(json_obj) + "\n"