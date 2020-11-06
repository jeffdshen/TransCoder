# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#

import itertools
import subprocess
import json
from pathlib import Path

import preprocessing.src.code_tokenizer as code_tokenizer
import preprocessing.src.python_tokenizer as code_compiler

from preprocessing.src.utils import (
    split_file,
    shuf_file,
    apply_bpe_file,
    get_vocab_file,
    learn_bpe_file,
    regroup_and_select_data,
    LocalExecutor,
    binarize_for_XLM_file,
    get_nlines,
    process_and_tokenize_json_file,
    map_dataset,
)

# extract_mode in {"", "sa", "cls"}
def process_language_pair_json_line(line, lang1, lang2, keep_comments, extract_mode):
    item = json.loads(line)
    if lang1 not in item:
        return None

    detok1 = getattr(code_tokenizer, f"detokenize_{lang1}")
    toker1 = getattr(code_tokenizer, f"tokenize_{lang1}")
    toker2 = getattr(code_tokenizer, f"tokenize_{lang2}")
    comp = getattr(code_compiler, f"{lang1}_to_{lang2}")

    file1 = item[lang1]
    if lang2 in item:
        file2 = item[lang2]
    elif extract_mode == "":
        file2 = comp(file1)
    else:
        file2 = None

    if file2 is not None:
        tok1 = toker1(file1)
        tok2 = toker2(file2)
        if len(tok1) > 0 and len(tok2) > 0:
            return json.dumps({lang1: " ".join(tok1), lang2: " ".join(tok2)}) + "\n"
        else:
            return None

    ex1 = getattr(code_tokenizer, f"extract_functions_{lang1}")
    ex2 = getattr(code_tokenizer, f"extract_functions_{lang2}")

    tok1 = toker1(file1)
    f1_sa, f1_cls = ex1(tok1)

    if extract_mode == "sa":
        f1_all = f1_sa
    elif extract_mode == "cls":
        f1_all = f1_cls
    else:
        return None

    results = []
    for f1 in f1_all:
        f2 = comp(detok1(f1))
        if f2 is None:
            continue

        f2_sa, f2_cls = ex2(toker2(f2))
        if len(f2_sa) + len(f2_cls) != 1:
            continue
        f2_all = f2_sa + f2_cls

        results.append(
            json.dumps({lang1: " ".join(f1), lang2: " ".join(f2_all[0])}) + "\n"
        )

    if len(results) == 0:
        return None
    return "".join(results)


def process_language_pair_json(input_path, lang1, lang2, keep_comments, extract_mode):
    suffix = ".with_comments" if keep_comments else ""
    output_path = input_path.with_suffix("").with_suffix(suffix + ".tok.json")
    map_dataset(
        input_path,
        output_path,
        process_language_pair_json_line,
        lang1=lang1,
        lang2=lang2,
        keep_comments=keep_comments,
        extract_mode=extract_mode,
        progress_bar=False,
    )


def select_toks(line, lang, **kwargs):
    json_obj = json.loads(line)
    assert lang in json_obj, f"{line} is missing {lang} field"
    return json_obj[lang] + "\n"


def select_toks_json(lang, input_path, output_path):
    map_dataset(
        input_path,
        output_path,
        select_toks,
        lang=lang,
        progress_bar=False,
    )


class LanguagePair:
    def __init__(self, root, lang1, lang2):
        self.root = Path(root)
        self.folder = Path(str(root)).joinpath(f"{lang1}-{lang2}")
        self.lang1 = lang1
        self.lang2 = lang2
        assert self.folder.is_dir(), (
            f"failed to initalize LanguagePair {lang1}-{lang2}, "
            f"there is no directory {str(self.folder)}"
        )

        self.folder_lang1 = self.root.joinpath(self.lang1)
        self.folder_lang2 = self.root.joinpath(self.lang2)
        if not self.folder_lang1.is_dir():
            self.folder_lang1.mkdir()

        if not self.folder_lang2.is_dir():
            self.folder_lang2.mkdir()

    def process_json_and_tok(self, keep_comments, extract_mode, executor=None):
        if executor is None:
            executor = LocalExecutor()
        suffix = ".with_comments" if keep_comments else ""
        jsons = list(self.folder.glob("*.[0-9][0-9][0-9].json.gz"))
        assert (
            len(jsons) > 0
        ), f"there is no *.[0-9][0-9][0-9].json.gz in {str(self.folder)}"

        jsons = [
            json
            for json in jsons
            if not json.with_suffix("").with_suffix(suffix + ".tok.json").is_file()
        ]
        print(f"{self.lang1}-{self.lang2}: processing {len(jsons)} json files ...")
        if len(jsons) > 0:
            jobs = executor.map_array(
                process_language_pair_json,
                jsons,
                itertools.repeat(self.lang1),
                itertools.repeat(self.lang2),
                itertools.repeat(keep_comments),
                itertools.repeat(extract_mode),
            )
            for job in jobs:
                job.result()

        # join
        all_tok = self.folder.joinpath(f"all{suffix}.tok.json")
        command = (
            f"cd {self.folder}; cat *.[0-9][0-9][0-9]{suffix}.tok.json > {all_tok}"
        )
        proc = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            executable="/bin/bash",
        )

        # shuf
        shuf_file(all_tok)

        # extract to language toks
        jobs = executor.map_array(
            select_toks_json,
            [self.lang1, self.lang2],
            itertools.repeat(all_tok),
            [
                self.folder_lang1.joinpath(f"all{suffix}.tok"),
                self.folder_lang2.joinpath(f"all{suffix}.tok"),
            ],
        )


class Language:
    def __init__(self, root, lang):
        self.folder = Path(str(root)).joinpath(lang)
        self.l = lang
        assert (
            self.folder.is_dir()
        ), f"failed to initalize Language {self.l}, there is no directory {str(self.folder)}"

    def process_json_and_tok(self, keep_comments, extract_mode, executor=None):
        print(f"{self.l}: process ...")

        if executor is None:
            executor = LocalExecutor()
        suffix = ".with_comments" if keep_comments else ""
        assert (
            len(list(self.folder.glob("*.json.gz"))) > 0
        ), f"there is no json in {str(self.folder)}"
        jsons = [
            json
            for json in self.folder.glob("*.json.gz")
            if not Path(str(json).replace(".json.gz", suffix + ".tok")).is_file()
        ]
        print(f"{self.l}: tokenizing {len(jsons)} json files ...")
        if len(jsons) > 0:
            jobs = executor.map_array(
                process_and_tokenize_json_file,
                jsons,
                itertools.repeat(self.l),
                itertools.repeat(keep_comments),
                itertools.repeat(extract_mode),
            )
            for job in jobs:
                job.result()

        # join
        all_tok = self.folder.joinpath(f"all{suffix}.tok")
        command = f"cd {self.folder}; cat *.[0-9][0-9][0-9]{suffix}.tok > {all_tok}"
        proc = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            executable="/bin/bash",
        )

        # shuf
        shuf_file(all_tok)

    def split_train_test_valid(self, keep_comments, test_size):
        suffix = ".with_comments" if keep_comments else ""
        all_tok = self.folder.joinpath(f"all{suffix}.tok")

        # select test/valid/train and split train in 8
        valid_file = self.folder.joinpath(f"valid{suffix}.tok")
        test_file = self.folder.joinpath(f"test{suffix}.tok")

        n_tests = 0

        if not valid_file.is_file():
            print(f"{self.l}: splitting valid ... ")
            subprocess.run(
                f"cat {all_tok} | head -n {test_size} > {valid_file}",
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            n_tests += test_size

        if not test_file.is_file():
            print(f"{self.l}: splitting test ... ")
            subprocess.run(
                f"cat {all_tok} | head -n {2 * test_size} | tail -n {test_size}  > {test_file}",
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            n_tests += test_size

        if not all(
            self.folder.joinpath(f"train{suffix}.{n}.tok").is_file() for n in range(8)
        ):
            print(f"{self.l}: splitting train ... ")
            n_lines = get_nlines(all_tok)
            split_len = int((n_lines - n_tests) / 8)
            for n, i in zip(range(8), range(2 * test_size, n_lines, split_len)):
                subprocess.run(
                    f"cat {all_tok} | head -n {i + split_len} | tail -n {split_len}  > {self.folder.joinpath(f'train{suffix}.{n}.tok')}",
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )

        n_lines = get_nlines(self.folder.joinpath(f"train{suffix}.0.tok"))
        size_gb = self.folder.joinpath(f"train{suffix}.0.tok").stat().st_size

        print(f"{self.l}: Finished splitting train, test and valid.")
        print(f"{self.l}: train 0 is {n_lines} lines and {size_gb / (1024 ** 3)} Go. ")
        return n_lines, size_gb


class Dataset:
    def __init__(self, root, langs, keep_comments, test_size, extract_mode):
        self.test_size = test_size
        self.root = Path(root)
        assert (
            self.root.is_dir()
        ), f"failed to build the dataset, there is no directory {str(root)}"

        if len(langs) == 1:
            lang1, lang2 = langs[0].split("-")
            self.lang_pair = LanguagePair(self.root, lang1, lang2)
            self.langs = [Language(root, lang) for lang in [lang1, lang2]]
        else:
            assert all(
                "-" not in lang for lang in langs
            ), "Language pair not allowed with other languages: {langs}"
            self.lang_pair = None
            self.langs = [Language(root, lang) for lang in langs]

        self.keep_comments = keep_comments
        self.extract_mode = extract_mode
        self.suffix = ".with_comments" if keep_comments else ""
        self.folder = self.root.joinpath(f"processed{self.suffix}")
        self.codes = self.folder.joinpath("codes")
        self.vocab = self.folder.joinpath("vocab")
        self.sizes = {l.l: [] for l in self.langs}
        if not self.folder.is_dir():
            self.folder.mkdir()

    def process_languages(
        self, lang_executor=None, tok_executor=None, split_executor=None
    ):
        if lang_executor is None:
            lang_executor = LocalExecutor()

        if self.lang_pair is not None:
            self.lang_pair.process_json_and_tok(
                self.keep_comments, self.extract_mode, tok_executor
            )
        else:
            jobs = [
                lang_executor.submit(
                    lang.process_json_and_tok,
                    self.keep_comments,
                    self.extract_mode,
                    tok_executor,
                )
                for lang in self.langs
            ]
            for job in jobs:
                job.result()

        jobs = [
            lang_executor.submit(
                lang.split_train_test_valid, self.keep_comments, self.test_size
            )
            for lang in self.langs
        ]
        for i, lang in enumerate(self.langs):
            self.sizes[lang.l] = jobs[i].result()

    def train_bpe(self, ncodes, size_gb=None):

        if self.codes.is_file():
            print("bpe codes already exists.")
            return

        print("train bpe ...")
        if size_gb is None:
            nlines = None
        else:
            size_gb_ = size_gb / len(self.langs)
            nlines = [
                int(self.sizes[l.l][0] * size_gb_ * 1024 ** 3 / self.sizes[l.l][1])
                for l in self.langs
            ]
            print(
                f"we need to regroup {nlines} lines for {self.langs[0].l} {self.langs[1].l} and {self.langs[2].l} to gather {size_gb} Go"
            )
        # train bpe on only 50 GB (25 each lang) of the tokenized train set
        data_train_bpe = self.folder.joinpath(f"train{self.suffix}.tok.{size_gb}GB")
        print(f"regroup and select data for training bpe in {data_train_bpe} ...")
        regroup_and_select_data(
            files=[l.folder.glob(f"train{self.suffix}.[0-9].tok") for l in self.langs],
            nlines=nlines,
            output=data_train_bpe,
        )

        print(f"training bpe on {data_train_bpe}...")
        learn_bpe_file(data_train_bpe, ncodes, self.codes)

    def get_vocab(self, size_gb=None):

        if self.vocab.is_file():
            print("vocab already exists.")
            return

        print("get vocab ...")
        if size_gb is None:
            nlines = None
        else:
            size_gb_ = size_gb / len(self.langs)
            nlines = [
                int(self.sizes[l.l][0] * size_gb_ * 1024 ** 3 / self.sizes[l.l][1])
                for l in self.langs
            ]
        # get vocab only from a subset of 40GB (20 each lang) of the bpe-ed train set
        data_get_vocab = self.folder.joinpath(f"train{self.suffix}.bpe.{size_gb}GB")
        print(f"regroup and select data in {data_get_vocab} to get vocab ...")
        regroup_and_select_data(
            files=[
                self.folder.glob(f"{l.l}.train{self.suffix}.[0-9].bpe")
                for l in self.langs
            ],
            nlines=nlines,
            output=data_get_vocab,
        )
        print(f"computing vocab on {data_get_vocab}...")
        get_vocab_file(data_get_vocab, self.vocab)

    def apply_bpe(self, files_regex, use_vocab=False, executor=None):
        vocab = "" if use_vocab is False else self.vocab
        if executor is None:
            executor = LocalExecutor()
        jobs = []
        for l in self.langs:
            for f in l.folder.glob(files_regex):
                out = self.folder.joinpath(f"{l.l}.{f.name}").with_suffix(".bpe")
                if not out.is_file():
                    print(f"apply bpe on {f} ...")
                    jobs.append(
                        executor.submit(apply_bpe_file, f, out, self.codes, vocab)
                    )
        for job in jobs:
            job.result()

    def cat_bpe(self, files_regex, out):
        for l in self.langs:
            out_file = self.folder.joinpath(f"{l.l}.{out}")
            for f in l.folder.glob(files_regex):
                if not out_file.is_file():
                    command = f"cd {self.folder}; cat {l.l}.{files_regex} > {l.l}.{out}"
                    proc = subprocess.run(
                        command,
                        shell=True,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        executable="/bin/bash",
                    )

    def binarize_for_XLM(self, files_regex, executor=None):
        print(f"binarize {files_regex} ...")
        if executor is None:
            executor = LocalExecutor()
        jobs = []
        for l in self.langs:
            for f in self.folder.glob(f"{l.l}.{files_regex}"):
                if not Path(str(f) + ".pth").is_file():
                    print(f"binarizing {f} ...")
                    jobs.append(executor.submit(binarize_for_XLM_file, f, self.vocab))
        for job in jobs:
            job.result()
