from errors import *
class Stack:  # Обычная реализация стека
    """
    Класс, реализующий стек, с основными методами.

    Основные методы:
    1. push - добавляет элемент в стек
    2. pop - удаляет элемент из стека
    3. is_empty - проверяет пустой ли стек
    """

    def __init__(self, *args):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            raise IndexError("Недостаточно операндов")
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])


def factorial(n: int) -> int:
    if n < 0:
        raise NegativeFactorialError(n)

    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def factorial_recursive(n: int) -> int:
    if n < 0:
        raise NegativeFactorialError(n)

    if n > 1:
        return n * factorial_recursive(n - 1)
    else:
        return 1


def fibo(n: int) -> int:
    a, b, res = 1, 1, 1
    for i in range(n - 2):
        res = a + b
        a = b
        b = res
    return res


def fibo_recursive(n: int) -> int:
    if n >= 3:
        return fibo_recursive(n - 1) + fibo_recursive(n - 2)
    else:
        return 1


def main():
    print(fibo_recursive(4))


if __name__ == "__main__":
    main()
