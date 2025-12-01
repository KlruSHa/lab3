class NegativeFactorialError(ValueError):
    """Исключение, выбрасываемое при попытке вычислить факториал отрицательного числа"""
    def __init__(self, value):
        self.value = value
        message = f"Факториал не определен для отрицательных чисел: {value}"
        super().__init__(message)