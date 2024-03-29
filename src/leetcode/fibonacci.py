# fibonacci.py


def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number.

    Args:
        n (int): The index of the Fibonacci number to calculate.

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[-1] + fib[-2])
        return fib[n]
