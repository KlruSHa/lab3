from src.errors import NegativeFibonacciError, NonIntegerError


def fibo_recursive(n: int) -> int:
    if n < 0:
        raise NegativeFibonacciError(n)
    if not isinstance(n, int):
        raise NonIntegerError("Fibonacci", type(n))

    if n >= 3:
        return fibo_recursive(n - 1) + fibo_recursive(n - 2)
    else:
        return 1