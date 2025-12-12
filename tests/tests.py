import pytest
from src.factorial_func import factorial
from src.factorial_recursive_func import factorial_recursive
from src.fibo_func import fibo
from src.fibo_recursive_func import fibo_recursive
from src.data_structures import Stack
from src.errors import NegativeFactorialError, NonIntegerError, NegativeFibonacciError, EmptyStackError
from src.sort.bubble_sort import bubble_sort
from src.sort.bucket_sort import bucket_sort
from src.sort.counting_sort import counting_sort
from src.sort.heap_sort import heap_sort
from src.sort.insertion_sort import insertion_sort
from src.sort.quick_sort import quick_sort
from src.sort.radix_sort import radix_sort


class TestFactorial:
    @pytest.mark.parametrize("n, expected", [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),])
    def test_factorial_valid(self, n, expected):
        assert factorial(n) == expected

    def test_factorial_negative(self):
        with pytest.raises(NegativeFactorialError):
            factorial(-10)

    def test_factorial_non_integer(self):
        with pytest.raises((NonIntegerError, TypeError)):
            factorial("5")

        with pytest.raises((NonIntegerError, TypeError)):
            factorial([1, 2, 3])


class TestFactorialRecursive:
    @pytest.mark.parametrize("n, expected", [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24)])
    def test_factorial_recursive_valid(self, n, expected):
        assert factorial_recursive(n) == expected

    def test_factorial_recursive_negative(self):
        with pytest.raises(NegativeFactorialError):
            factorial_recursive(-10)

    def test_factorial_recursive_non_integer(self):
        with pytest.raises((NonIntegerError, TypeError)):
            factorial_recursive("5")


class TestFibo:
    @pytest.mark.parametrize("n, expected", [
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21)])
    def test_fibo_valid(self, n, expected):
        assert fibo(n) == expected

    def test_fibo_negative(self):
        with pytest.raises(NegativeFibonacciError):
            fibo(-10)

    def test_fibo_non_integer(self):
        with pytest.raises((NonIntegerError, TypeError)):
            fibo("5")


class TestFiboRecursive:
    @pytest.mark.parametrize("n, expected", [
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21)])
    def test_fibo_recursive_valid(self, n, expected):
        assert fibo_recursive(n) == expected

    def test_fibo_recursive_negative(self):
        with pytest.raises(NegativeFibonacciError):
            fibo_recursive(-10)

    def test_fibo_recursive_non_integer(self):
        with pytest.raises((NonIntegerError, TypeError)):
            fibo_recursive("5")


class TestStack:
    def test_stack_init(self):
        stack = Stack()
        assert stack.is_empty()
        assert len(stack) == 0

    def test_stack_push_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        assert stack.pop() == 2
        assert stack.pop() == 1
        assert stack.is_empty()

    def test_stack_peek(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        assert stack.peek() == 20

    def test_stack_is_empty(self):
        stack = Stack()
        assert stack.is_empty()
        
        stack.push(1)
        assert not stack.is_empty()
        
        stack.pop()
        assert stack.is_empty()

    def test_stack_len(self):
        stack = Stack()
        assert len(stack) == 0
        stack.push(1)
        assert len(stack) == 1
        stack.push(1)
        assert len(stack) == 2

    def test_stack_min(self):
        stack = Stack()
        stack.push(5)
        assert stack.min() == 5
        
        stack.push(3)
        assert stack.min() == 3
        
        stack.push(7)
        assert stack.min() == 3
        
        stack.push(2)
        assert stack.min() == 2
        
        stack.pop()
        assert stack.min() == 3
        
        stack.pop()
        assert stack.min() == 3
        
        stack.pop()
        assert stack.min() == 5

    def test_stack_pop_empty(self):
        stack = Stack()
        with pytest.raises(EmptyStackError) as exc_info:
            stack.pop()
        assert exc_info.value.operation == "pop"

    def test_stack_peek_empty(self):
        stack = Stack()
        with pytest.raises(EmptyStackError) as exc_info:
            stack.peek()
        assert exc_info.value.operation == "peek"

    def test_stack_min_empty(self):
        stack = Stack()
        with pytest.raises(EmptyStackError) as exc_info:
            stack.min()
        assert exc_info.value.operation == "min"


class TestBubbleSort:
    @pytest.mark.parametrize("input_list, expected", [
        ([3, 1, 4, 1, 5, 9, 2, 6], [1, 1, 2, 3, 4, 5, 6, 9]),
        ([5, 2, 8, 1, 9], [1, 2, 5, 8, 9]),
        ([1], [1]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([-3, 1, -1, 5, 0], [-3, -1, 0, 1, 5]),
        ([], []),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])])
    def test_bubble_sort_valid(self, input_list, expected):
        result = bubble_sort(input_list.copy())
        assert result == expected


class TestBucketSort:
    @pytest.mark.parametrize("input_list, expected", [
        ([0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51], 
         [0.32, 0.33, 0.37, 0.42, 0.47, 0.51, 0.52]),
        ([0.1, 0.9, 0.5, 0.3, 0.7], [0.1, 0.3, 0.5, 0.7, 0.9]),
        ([0.5], [0.5]),
        ([], []),
        ([0.5, 0.5, 0.5], [0.5, 0.5, 0.5]),
        ([0.1, 0.2, 0.3], [0.1, 0.2, 0.3])])
    def test_bucket_sort_valid(self, input_list, expected):
        result = bucket_sort(input_list.copy())
        assert result == expected

    def test_bucket_sort_custom_base(self):
        result = bucket_sort([0.1, 0.9, 0.5, 0.3, 0.7], base=5)
        assert result == [0.1, 0.3, 0.5, 0.7, 0.9]


class TestCountingSort:
    @pytest.mark.parametrize("input_list, expected", [
        ([4, 2, 2, 8, 3, 3, 1], [1, 2, 2, 3, 3, 4, 8]),
        ([5, 2, 8, 1, 9], [1, 2, 5, 8, 9]),
        ([1], [1]),
        ([], []),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([-3, 1, -1, 5, 0], [-3, -1, 0, 1, 5]),
        ([3, 3, 3, 1, 1, 2], [1, 1, 2, 3, 3, 3])])
    def test_counting_sort_valid(self, input_list, expected):
        result = counting_sort(input_list.copy())
        assert result == expected

    def test_counting_sort_non_integer(self):
        with pytest.raises(NonIntegerError):
            counting_sort([1, "2", 3])


class TestHeapSort:
    @pytest.mark.parametrize("input_list, expected", [
        ([4, 10, 3, 5, 1], [1, 3, 4, 5, 10]),
        ([5, 2, 8, 1, 9], [1, 2, 5, 8, 9]),
        ([1], [1]),
        ([], []),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([-3, 1, -1, 5, 0], [-3, -1, 0, 1, 5]),
        ([3, 3, 3, 1, 1, 2], [1, 1, 2, 3, 3, 3])])
    def test_heap_sort_valid(self, input_list, expected):
        result = heap_sort(input_list.copy())
        assert result == expected


class TestInsertionSort:
    @pytest.mark.parametrize("input_list, expected", [
        ([4, 3, 2, 1], [1, 2, 3, 4]),
        ([5, 2, 8, 1, 9], [1, 2, 5, 8, 9]),
        ([1], [1]),
        ([], []),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([-3, 1, -1, 5, 0], [-3, -1, 0, 1, 5]),
        ([3, 3, 3, 1, 1, 2], [1, 1, 2, 3, 3, 3])])
    def test_insertion_sort_valid(self, input_list, expected):
        test_list = input_list.copy()
        insertion_sort(test_list)
        assert test_list == expected


class TestQuickSort:
    @pytest.mark.parametrize("input_list, expected", [
        ([4, 2, 7, 1, 9, 3], [1, 2, 3, 4, 7, 9]),
        ([5, 2, 8, 1, 9], [1, 2, 5, 8, 9]),
        ([1], [1]),
        ([], []),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([-3, 1, -1, 5, 0], [-3, -1, 0, 1, 5]),
        ([3, 3, 3, 1, 1, 2], [1, 1, 2, 3, 3, 3])])
    def test_quick_sort_valid(self, input_list, expected):
        result = quick_sort(input_list.copy())
        assert result == expected


class TestRadixSort:
    @pytest.mark.parametrize("input_list, expected", [
        ([170, 45, 75, 90, 2, 802, 24, 66], [2, 24, 45, 66, 75, 90, 170, 802]),
        ([5, 2, 8, 1, 9], [1, 2, 5, 8, 9]),
        ([1], [1]),
        ([], []),
        ([3, 3, 3, 1, 1, 2], [1, 1, 2, 3, 3, 3])])
    def test_radix_sort_valid(self, input_list, expected):
        result = radix_sort(input_list.copy())
        assert result == expected

    def test_radix_sort_custom_base(self):
        result = radix_sort([170, 45, 75, 90, 2, 802, 24, 66], base=8)
        assert result == [2, 24, 45, 66, 75, 90, 170, 802]


    def test_radix_sort_non_integer(self):
        with pytest.raises(NonIntegerError):
            radix_sort([1, "2", 3])
