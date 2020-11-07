# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#

import subprocess
import typing as tp
import io
import pathlib
from pathlib import Path
import json
import fileinput
import os
from multiprocessing import Pool, cpu_count
import tqdm
import gzip

from preprocessing.src import code_tokenizer as code_tokenizer
from preprocessing.src.timeout import timeout, TimeoutError

FAST = str(Path(__file__).parents[2].joinpath("XLM/tools/fastBPE/fast"))
XLM_PP = str(Path(__file__).parents[2].joinpath("XLM/preprocess.py"))

FALSY_STRINGS = {"off", "false", "0"}
TRUTHY_STRINGS = {"on", "true", "1"}


def bool_flag(s):
    """
    Parse boolean arguments from the command line.
    """
    if s.lower() in FALSY_STRINGS:
        return False
    elif s.lower() in TRUTHY_STRINGS:
        return True
    else:
        raise argparse.ArgumentTypeError("Invalid value for a boolean flag!")


def map_dataset_helper(input_file, output_file, func, progress_bar=None, **kwargs):
    for line in input_file:
        output_line = func(line, **kwargs)
        if output_line is not None:
            output_file.write(output_line)

        if progress_bar is not None:
            progress_bar.update(len(line.encode()))


def map_dataset(input_path, output_path, func, progress_bar=True, **kwargs):
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
                map_dataset_helper(
                    input_file, output_file, func, progress_bar=pbar_to_pass, **kwargs
                )


def tokenize_json_helper(inpt):
    tokenizer, content, keep_comments = inpt
    content_tokenized = tokenizer(content, keep_comments)
    return " ".join(content_tokenized)


@timeout(3600)
def output_all_tokenized_results(docs, f_tok, ex, extract_mode):
    pool = Pool(cpu_count())
    result_content_tokenized = tqdm.tqdm(
        pool.imap_unordered(tokenize_json_helper, docs), total=len(docs)
    )

    if extract_mode == "":
        for content_tokenized in result_content_tokenized:
            if len(content_tokenized) == 0:
                continue
            # for some reason sometimes, some characters of s
            # cannot be encoded into utf-8 and it failed to print, so use try/catch
            try:
                f_tok.write(content_tokenized)
                f_tok.write("\n")
            except:
                continue
        return

    result_functions = tqdm.tqdm(
        pool.imap_unordered(ex, result_content_tokenized),
        total=len(result_content_tokenized),
    )
    
    for func_standalone, func_class in result_functions:
        if extract_mode == "sa":
            funcs = func_standalone
        elif extract_mode == "cls":
            funcs = func_class

        for func in funcs:         
            # for some reason sometimes, some caracters of s
            # cannot be encoded into utf-8 and it failed to print, so use try/catch
            try:
                f_tok.write(func)
                f_tok.write("\n")
            except:
                continue


def process_and_tokenize_json_file(input_path, language, keep_comments, extract_mode):
    suffix = ".with_comments" if keep_comments else ""
    output_path = str(input_path).replace(".json.gz", suffix + ".tok")
    tokenizer = getattr(code_tokenizer, f"tokenize_{language}")
    docs = []
    for line in fileinput.input(str(input_path), openhook=fileinput.hook_compressed):
        x = json.loads(line)
        content = x["content"]
        docs.append((tokenizer, content, keep_comments))

    f_tok = open(output_path, "w", encoding="utf-8")
    try:
        ex = getattr(code_tokenizer, f"extract_functions_{language}")
        output_all_tokenized_results(docs, f_tok, ex, extract_mode)
    except TimeoutError:
        # The tokenization process is sometimes killed and it makes the multiprocessing hang forever
        f_tok.close()
        print("Program closed automatically after one hour")
        os._exit(0)


def get_nlines(file_path):
    assert file_path.is_file()
    process = subprocess.run(
        f"wc -l {file_path}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    if process.returncode == 0:
        return int(process.stdout.decode().split(" ")[0])
    else:
        return None


def head(file_path, n):
    n = int(n)
    with file_path.open("r", encoding="utf-8") as f:
        h = [next(f) for i in range(n)]
    return h


def write_head(file_path, n):
    n = int(n)
    with file_path.open("r", encoding="utf-8") as f:
        h = [next(f) for i in range(n)]
    with file_path.open("w", encoding="utf-8") as f:
        f.write("".join(h))
    return h


def split_file(file_path, num_files=None):
    if num_files is None:
        num_files = cpu_count()

    if any(Path(f"{file_path}.{n}").is_file() for n in range(num_files)):
        print(f"{file_path}: a split file already exists.")
        return

    process = subprocess.run(
        f"split -n l/{num_files} {file_path}.",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert process.returncode == 0, f"failed to split {file_path}"


def shuf_file(file_path):
    process = subprocess.run(
        f"shuf {file_path} -o {file_path}",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert process.returncode == 0, f"failed to shuffle {file_path}"


def apply_bpe_file(file_path, output, codes, vocab=None):
    if vocab is None:
        vocab = ""
    process = subprocess.run(
        f"{FAST} applybpe {output} {file_path} {codes} {vocab}",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert (
        Path(output).is_file and process.returncode == 0
    ), f"failed to apply bpe on {file_path}, command: \n {FAST} applybpe {output} {file_path} {codes} {vocab}"


def learn_bpe_file(file_path, ncodes, codes):
    process = subprocess.run(
        f"{FAST} learnbpe {ncodes} {file_path} > {str(codes)} ",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert process.returncode == 0, f"failed to learn bpe on {str(file_path)}"
    assert Path(
        f"{str(codes)}"
    ).is_file, f"failed to output codes, cannot find codes {str(codes)}"
    if ncodes > 50000:
        codes.write_text("".join(head(codes, 50000)), encoding="utf-8")


def get_vocab_file(file_path, vocab):
    process = subprocess.run(
        f"{FAST} getvocab {file_path} > {str(vocab)}.all",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    process2 = subprocess.run(
        f"head -n 64000 {str(vocab)}.all > {str(vocab)}",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert (
        vocab.is_file and process.returncode == 0 and process2.returncode == 0
    ), f"failed to get vocab for {file_path}"


def binarize_for_XLM_file(file_path, vocab):
    process = subprocess.run(
        f"python {XLM_PP} {vocab} {file_path}",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert (
        Path(f"{file_path}.pth").is_file and process.returncode == 0
    ), f"failed to binarize for XLM the file {file_path} \n command: python {XLM_PP} {vocab} {file_path} "


def regroup_and_select_data(files, output, nlines=None):
    """
    files : [files] or [[files1],[files2]]
    nlines : [n1]
    if files = [files] it will regroup files, shuffle them and select nlines[0] of itselfself. write the res in output.
    if files = [[files1],[files2]] it will regroup, shuffle and select nlines[0] lines files1 (resp. files2),
    and concat these res in ouput.
    """
    if output.is_file():
        return

    assert nlines is None or len(files) == len(nlines)
    if nlines is None:
        nlines = [float("Inf") for i in range(len(files))]

    for files_, nlines_ in zip(files, nlines):
        missing_lines = nlines_
        for f in files_:
            n = get_nlines(f)
            if n < missing_lines:
                print(f"adding {n} lines of {f}")
                proc = subprocess.run(
                    f"cat {f} >> {output}",
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    executable="/bin/bash",
                )
                missing_lines = missing_lines - n
            else:
                print(f"adding {missing_lines} lines of {f}")
                proc = subprocess.run(
                    f"cat {f} | head -n {missing_lines} >> {output}",
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    executable="/bin/bash",
                )
                break


def create_symlink(file_path, symlink):
    assert file_path.is_file(), file_path
    assert not symlink.is_file(), symlink
    process = subprocess.run(
        f"ln -s {file_path} {symlink}",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert (
        symlink.is_file() and process.returncode == 0
    ), f"failed to create symlink {symlink} for file {file_path} "


class DelayedJob:
    """Future-like object which delays computation"""

    def __init__(
        self, func: tp.Callable[..., tp.Any], *args: tp.Any, **kwargs: tp.Any
    ) -> None:
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self._result: tp.Optional[tp.Any] = None
        self._computed = False

    def done(self) -> bool:
        return True

    def result(self) -> tp.Any:
        if not self._computed:
            self._result = self.func(*self.args, **self.kwargs)
            self._computed = True
        return self._result


class LocalExecutor:
    """Executor which run sequentially and locally
    (just calls the function and returns a FinishedJob)
    """

    def submit(
        self, fn: tp.Callable[..., tp.Any], *args: tp.Any, **kwargs: tp.Any
    ) -> DelayedJob:
        return DelayedJob(fn, *args, **kwargs)

    def map_array(self, fn, *arg_iterators):
        grouped_args = zip(*arg_iterators)
        return [self.submit(fn, *g) for g in grouped_args]

def map_array(executor, fn, *arg_iterators):
    if hasattr(executor, 'map_array'):
        return executor.map_array
    
    grouped_args = zip(*arg_iterators)
    return [executor.submit(fn, *g) for g in grouped_args]