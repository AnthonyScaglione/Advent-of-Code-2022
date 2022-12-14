#!/usr/bin/env python3

# ty github.com/gorel for utils :)

import argparse
import os
from typing import Callable, Optional, Tuple, TypeVar

T1 = TypeVar("T1")
T2 = TypeVar("T2")

SolveFunc = Callable[[str], Tuple[T1, T2]]

DEFAULT_TEST_INPUT_NAME = "sample_data.txt"
DEFAULT_INPUT_NAME = "input_data.txt"


def get_parser(input_filepath: str, test_filepath: str) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input-file", default=input_filepath)
    parser.add_argument("-t", "--test-file", default=test_filepath)
    return parser


def get_default_test_input_path(main_file: str) -> str:
    directory = os.path.dirname(main_file)
    return os.path.join(directory, DEFAULT_TEST_INPUT_NAME)


def get_default_input_path(main_file: str) -> str:
    directory = os.path.dirname(main_file)
    return os.path.join(directory, DEFAULT_INPUT_NAME)


def generate_festivity(
    main_file: str,
    solve: SolveFunc[T1, T2],
    test_solution1: Optional[T1] = None,
    test_solution2: Optional[T2] = None,
) -> None:
    parser = get_parser(
        get_default_input_path(main_file), get_default_test_input_path(main_file)
    )
    args = parser.parse_args()

    res1, res2 = solve(args.test_file)
    if test_solution1 is not None:
        assert (
            res1 == test_solution1
        ), f"Failed test for part 1; {res1} != {test_solution1}"
    if test_solution2 is not None:
        assert (
            res2 == test_solution2
        ), f"Failed test for part 2; {res2} != {test_solution2}"

    res1, res2 = solve(args.input_file)
    print(f"Solution 1: {res1}")
    print(f"Solution 2: {res2}")