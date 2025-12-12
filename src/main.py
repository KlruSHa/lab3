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
    if len(a) <= 1:
        return a

    left = []
    mid = []
    right = []
    pivot = a[len(a) // 2]

    for elem in a:
        if elem < pivot:
            left.append(elem)
        elif elem > pivot:
            right.append(elem)
        else:
            mid.append(elem)
    return quick_sort(left) + mid + quick_sort(right)


def counting_sort(a: list[int]) -> list[int]:
    m = max(a)
    c = [0] * (m + 1)
    res = []

    for elem in a:
        c[elem] += 1
    for i in range(len(c)):
        count = c[i]
        for j in range(count):
            res.append(i)
    return res


def radix_sort(a: list[int], base: int = 10) -> list[int]:
    bins = [[] for _ in range(base)]
    maxi = len(str(max(a)))

    for i in range(0, maxi):
        for elem in a:
            digit = (elem // (base ** i)) % base
            bins[digit].append(elem)
        a = []
        for i in bins:
            for j in i:
                a.append(j)

        bins = [[] for _ in range(base)]
    return a


def insertion_sort(b):
    for i in range(1, len(b)):
        key = b[i]
        j = i - 1
        while j >= 0 and key < b[j]:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = key


def bucket_sort(a: list[float], base: int = 10) -> list[float]:
    mini = min(a)
    maxi = max(a)
    d = maxi - mini

    if d == 0:
        return a

    bins = [[] for _ in range(base)]

    for elem in a:
        norm = (elem - mini) / d
        idx = int(base * norm)
        if idx == base:
            idx -= 1
        bins[idx].append(elem)

    a = []
    for b in bins:
        insertion_sort(b)
        for elem in b:
            a.append(elem)
    return a


def heap_sort(a: list[int]) -> list[int]:
    def sift(n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and a[l] > a[largest]:
            largest = l

        if r < n and a[r] > a[largest]:
            largest = r

        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            sift(n, largest)

    n = len(a)

    for i in range(n // 2 - 1, -1, -1):
        sift(n, i)

    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        sift(i, 0)

    return a


def main():
    a = [7, 3, 9, 2, 5, 8, 1, 6]
    print(heap_sort(a))


if __name__ == "__main__":
    main()
