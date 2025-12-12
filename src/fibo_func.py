from errors import NegativeFibonacciError, NonIntegerError


def fibo(n: int) -> int:
    if n < 0:
        raise NegativeFibonacciError(n)
    if not isinstance(n, int):
        raise NonIntegerError("Fibonacci", type(n))

    a, b, res = 1, 1, 1
    for i in range(n - 2):
        res = a + b
        a = b
        b = res
    return res
