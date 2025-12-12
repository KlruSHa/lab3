class NegativeFactorialError(ValueError):
    """Исключение, выбрасываемое при попытке вычислить факториал отрицательного числа"""
    def __init__(self, value):
        self.value = value
        message = f"Факториал не определен для отрицательных чисел: {value}"
        super().__init__(message)


class EmptyStackError(Exception):
    """Исключение, выбрасываемое при попытке доступа к элементам пустого стека"""
    def __init__(self, operation):
        self.operation = operation
        message = f"Невозможно выполнить операцию '{operation}': стек пуст"
        super().__init__(message)


class NegativeFibonacciError(ValueError):
    """Исключение, выбрасываемое при попытке вычислить число Фибоначчи для отрицательного числа"""
    def __init__(self, value):
        self.value = value
        message = f"Число Фибоначчи не определено для отрицательных чисел: {value}"
        super().__init__(message)


class NonIntegerError(TypeError):
    """Исключение, выбрасываемое, если алгоритм получает не целое число"""
    def __init__(self, algo_name, element_type):
        self.algo_name = algo_name
        self.element_type = element_type
        message = f"Алгоритм '{algo_name}' работает только с целыми числами. Обнаружен тип: {element_type}"
        super().__init__(message)
