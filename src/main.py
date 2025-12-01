from errors import *


class Stack:  # Обычная реализация стека
    """
    Класс, реализующий стек, с основными методами.

    Основные методы:
    1. push - добавляет элемент в стек
    2. pop - удаляет элемент из стека
    3. is_empty - проверяет пустой ли стек
    4. peek - показывает верхний эелмент стека
    5. __len__ - возвращает длину стека
    6. min - возвращает текущий минимум стека за O(1)
    """

    def __init__(self, *args):
        self.items = []
        self.min_item = []

    def push(self, item):
        self.items.append(item)
        if not self.min_item:
            self.min_item.append(item)
        else:
            if self.min_item[-1] >= item:
                self.min_item.append(item)

    def pop(self):
        if not self.items:
            raise IndexError("Удаление из пустого стека")
        if self.items[-1] == self.min_item[-1]:
            self.min_item.pop()
            return self.items.pop()
        else:
            return self.items.pop()

    def is_empty(self):
        return (self.items == [])

    def peek(self):
        if not self.items:
            raise IndexError("Просмотр пустого стека")
        return self.items[-1]

    def __len__(self):
        return len(self.items)

    def min(self) -> int:
        if not self.min_item:
            raise IndexError("Стек пуст")
        return self.min_item[-1]


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


def bubble_sort(a: list[int]) -> list[int]:
    for i in range(1, len(a) + 1):
        for j in range(len(a) - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def quick_sort(a: list[int]) -> list[int]:
    pass


def counting_sort(a: list[int]) -> list[int]:
    pass


def radix_sort(a: list[int], base: int = 10) -> list[int]:
    pass


def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]:
    pass


def heap_sort(a: list[int]) -> list[int]:
    pass


def main():
    print()


if __name__ == "__main__":
    main()
