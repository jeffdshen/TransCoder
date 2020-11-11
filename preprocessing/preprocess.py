# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#

import argparse
from concurrent.futures import ProcessPoolExecutor


from preprocessing.src.dataset import Dataset
from preprocessing.src.utils import bool_flag, create_symlink
from submitit import AutoExecutor
import subprocess
from pathlib import Path


def check_files_and_symlink_for_XLM(dataset, langs, extract_mode):
    # create symlink for all code - used for MLM pretraining
    print("check that all files exist...")
    for lang in langs:
        for i in range(8):
            assert dataset.folder.joinpath(
                f"{lang}.train{dataset.suffix}.{i}.bpe.pth"
            ).is_file()
        assert dataset.folder.joinpath(
            f"{lang}.train{dataset.suffix}.bpe.pth"
        ).is_file()
        assert dataset.folder.joinpath(f"{lang}.test{dataset.suffix}.bpe.pth").is_file()
        assert dataset.folder.joinpath(
            f"{lang}.valid{dataset.suffix}.bpe.pth"
        ).is_file()
    XLM_folder = Path(str(dataset.folder) + ".XLM-syml")
    XLM_folder.mkdir(exist_ok=True)
    print("create symlinks for XLM ...")
    suffix = "" if extract_mode == "" else "_" + extract_mode
    for lang in langs:
        for i in range(8):
            create_symlink(
                dataset.folder.joinpath(f"{lang}.train{dataset.suffix}.{i}.bpe.pth"),
                XLM_folder.joinpath(f"train.{lang}{suffix}.{i}.pth"),
            )

        create_symlink(
            dataset.folder.joinpath(f"{lang}.train{dataset.suffix}.bpe.pth"),
            XLM_folder.joinpath(f"train.{lang}{suffix}.pth"),
        )
        create_symlink(
            dataset.folder.joinpath(f"{lang}.valid{dataset.suffix}.bpe.pth"),
            XLM_folder.joinpath(f"valid.{lang}{suffix}.pth"),
        )
        create_symlink(
            dataset.folder.joinpath(f"{lang}.test{dataset.suffix}.bpe.pth"),
            XLM_folder.joinpath(f"test.{lang}{suffix}.pth"),
        )

    if len(langs) == 2:
        create_symlink(
            XLM_folder.joinpath(f"test.{langs[0]}{suffix}.pth"),
            XLM_folder.joinpath(f"test.{langs[0]}{suffix}-{langs[1]}{suffix}.{langs[0]}{suffix}.pth"),
        )
        create_symlink(
            XLM_folder.joinpath(f"test.{langs[1]}{suffix}.pth"),
            XLM_folder.joinpath(f"test.{langs[0]}{suffix}-{langs[1]}{suffix}.{langs[1]}{suffix}.pth"),
        )
        create_symlink(
            XLM_folder.joinpath(f"valid.{langs[0]}{suffix}.pth"),
            XLM_folder.joinpath(f"valid.{langs[0]}{suffix}-{langs[1]}{suffix}.{langs[0]}{suffix}.pth"),
        )
        create_symlink(
            XLM_folder.joinpath(f"valid.{langs[1]}{suffix}.pth"),
            XLM_folder.joinpath(f"valid.{langs[0]}{suffix}-{langs[1]}{suffix}.{langs[1]}{suffix}.pth"),
        )
        create_symlink(
            XLM_folder.joinpath(f"train.{langs[0]}{suffix}.pth"),
            XLM_folder.joinpath(f"train.{langs[0]}{suffix}-{langs[1]}{suffix}.{langs[0]}{suffix}.pth"),
        )
        create_symlink(
            XLM_folder.joinpath(f"train.{langs[1]}{suffix}.pth"),
            XLM_folder.joinpath(f"train.{langs[0]}{suffix}-{langs[1]}{suffix}.{langs[1]}{suffix}.pth"),
        )
        for i in range(8):
            create_symlink(
                XLM_folder.joinpath(f"train.{langs[0]}{suffix}.{i}.pth"),
                XLM_folder.joinpath(f"train.{langs[0]}{suffix}-{langs[1]}{suffix}.{langs[0]}{suffix}.{i}.pth"),
            )
            create_symlink(
                XLM_folder.joinpath(f"train.{langs[1]}{suffix}.{i}.pth"),
                XLM_folder.joinpath(f"train.{langs[0]}{suffix}-{langs[1]}{suffix}.{langs[1]}{suffix}.{i}.pth"),
            )



def preprocess(
    root,
    langs,
    keep_comments,
    local,
    extract_mode,
    test_size,
    ncodes=100000,
    size_gb=50,
):
    if size_gb < 1:
        size_gb = None
    dataset = Dataset(root, langs, keep_comments, test_size, extract_mode)
    if len(langs) == 1:
        langs = langs[0].split("-")
    langs = sorted(langs)

    with ProcessPoolExecutor() as mp_executor:
        if not local:
            dataset.folder.joinpath("log").mkdir()
            cluster_ex1 = AutoExecutor(dataset.folder.joinpath("log"))
            cluster_ex1.update_parameters(cpus_per_task=80, mem_gb=30, timeout_min=40)
            cluster_ex2 = AutoExecutor(dataset.folder.joinpath("log"))
            cluster_ex2.update_parameters(cpus_per_task=20, mem_gb=200, timeout_min=240)
        else:
            cluster_ex1 = None
            cluster_ex2 = None
        single_ex = mp_executor if cluster_ex2 is None else cluster_ex2

        dataset.process_languages(
            lang_executor=mp_executor,
            tok_executor=cluster_ex1,
            split_executor=cluster_ex2,
        )

        dataset.train_bpe(ncodes=ncodes, size_gb=size_gb)

        print("apply bpe on train ... ")
        dataset.apply_bpe(
            f"train{dataset.suffix}.[0-9].tok",
            use_vocab=False,
            executor=single_ex,
        )

        dataset.get_vocab(size_gb=size_gb)

        print("cat train ... ")
        dataset.cat_bpe(
            f"train{dataset.suffix}.[0-9].bpe",
            f"train{dataset.suffix}.bpe",
        )
        print("apply bpe on test and valid ...")
        dataset.apply_bpe(f"test{dataset.suffix}.tok", use_vocab=False, executor=None)
        dataset.apply_bpe(f"valid{dataset.suffix}.tok", use_vocab=False, executor=None)

        dataset.binarize_for_XLM(f"train{dataset.suffix}.[0-9].bpe", executor=single_ex)
        dataset.binarize_for_XLM(f"train{dataset.suffix}.bpe", executor=None)
        dataset.binarize_for_XLM(f"test{dataset.suffix}.bpe", executor=None)
        dataset.binarize_for_XLM(f"valid{dataset.suffix}.bpe", executor=None)

        check_files_and_symlink_for_XLM(dataset, langs, extract_mode)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("root", help="root folder")
    parser.add_argument(
        "--langs",
        help="comma-split languages or a language pair, e.g. cpp,python, or python-dis",
    )
    parser.add_argument("--test_size", type=int, default=1000, help="size of test set")
    parser.add_argument(
        "--bpe_train_size",
        type=int,
        default=50,
        help="size in GB of subset used to train bpe codes",
    )
    parser.add_argument(
        "--keep_comments",
        type=bool_flag,
        default=False,
        help="used bpe trained on data with comments or not",
    )
    parser.add_argument(
        "--local",
        type=bool_flag,
        default=True,
        help="True if you want to run the processing pipeline locally, false if want to use submitit.",
    )
    parser.add_argument(
        "--extract_mode",
        default="",
        choices=["", "sa", "cls"],
        help="no extraction, extract standalone functions, or extract class functions",
    )
    args = parser.parse_args()

    preprocess(
        args.root,
        args.langs.split(","),
        args.keep_comments,
        args.local,
        extract_mode=args.extract_mode,
        test_size=args.test_size,
        size_gb=args.bpe_train_size,
    )
