from errors import EmptyStackError


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
            raise EmptyStackError("pop")
        if self.items[-1] == self.min_item[-1]:
            self.min_item.pop()
            return self.items.pop()
        else:
            return self.items.pop()

    def is_empty(self):
        return not self.items

    def peek(self):
        if not self.items:
            raise EmptyStackError("peek")
        return self.items[-1]

    def __len__(self):
        return len(self.items)

    def min(self) -> int:
        if not self.min_item:
            raise EmptyStackError("min")
        return self.min_item[-1]
