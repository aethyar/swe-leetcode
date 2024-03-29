# test_fibonacci.py

import pytest

from src.leetcode.fibonacci import fibonacci


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (0, 0),  # Fibonacci of 0 is 0
        (1, 1),  # Fibonacci of 1 is 1
        (2, 1),  # Fibonacci of 2 is 1
        (3, 2),  # Fibonacci of 3 is 2
        (4, 3),  # Fibonacci of 4 is 3
        (5, 5),  # Fibonacci of 5 is 5
        (6, 8),  # Fibonacci of 6 is 8
        (7, 13),  # Fibonacci of 7 is 13
        (8, 21),  # Fibonacci of 8 is 21
        (9, 34),  # Fibonacci of 9 is 34
        (10, 55),  # Fibonacci of 10 is 55
    ],
)
def test_fibonacci(test_input: int, expected: int):
    assert fibonacci(test_input) == expected
