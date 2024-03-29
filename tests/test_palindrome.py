# test_palindrome.py

import pytest

from src.leetcode.palindrome import is_palindrome


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("", True),  # Empty string is considered a palindrome
        ("racecar", True),  # "racecar" is a palindrome
        ("A man, a plan, a canal, Panama", True),  # Ignoring spaces and punctuation
        ("hello", False),  # "hello" is not a palindrome
        ("Able was I, ere I saw Elba", True),  # Case-insensitive palindrome with spaces and punctuation
        ("12321", True),  # Numeric palindrome
        ("not a palindrome", False),  # Not a palindrome
    ],
)
def test_is_palindrome(test_input: str, expected: str):
    assert is_palindrome(test_input) == expected
