from src.leetcode.palindrome import is_palindrome


def test_palindrome_true():
    assert is_palindrome("level") is True
    assert is_palindrome("radar") is True
    assert is_palindrome("A man, a plan, a canal, Panama") is True
    assert is_palindrome("Was it a car or a cat I saw?") is True
    assert is_palindrome("Mr. Owl ate my metal worm") is True
    assert is_palindrome("") is True
    assert is_palindrome("a") is True
    assert is_palindrome("   ") is True
    assert is_palindrome(" ") is True
    assert is_palindrome("!?@#?!") is True
    assert is_palindrome("12321") is True
    assert is_palindrome("a!a") is True


def test_palindrome_false():
    assert is_palindrome("hello") is False
    assert is_palindrome("world") is False
    assert is_palindrome("Python") is False
    assert is_palindrome("Palindrome") is False
    assert is_palindrome("This is not a palindrome") is False
