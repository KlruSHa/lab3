from src.errors import *


def factorial_recursive(n: int) -> int:
    if n < 0:
        raise NegativeFactorialError(n)
    if not isinstance(n, int):
        raise NonIntegerError("Factorial", type(n))

    if n > 1:
        return n * factorial_recursive(n - 1)
    else:
        return 1