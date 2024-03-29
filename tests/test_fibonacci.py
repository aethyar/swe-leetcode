from src.leetcode.fibonacci import fibonacci


def test_fibonacci():
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
    assert fibonacci(9) == 34
    assert fibonacci(10) == 55


def test_fibonacci_zero():
    assert fibonacci(0) == 0


def test_fibonacci_negative():
    assert fibonacci(-1) == 0
