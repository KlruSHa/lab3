from src.errors import *


def factorial(n: int) -> int:
    if n < 0:
        raise NegativeFactorialError(n)
    if not isinstance(n, int):
        raise NonIntegerError("Factorial", type(n))

    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
