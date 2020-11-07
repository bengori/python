"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""


#  альтернативный вариант через встроенную функцию reduce()
from functools import reduce
my_list = [number for number in range(100, 1001) if number % 2 == 0]
print(reduce(lambda x, y: x * y, my_list))


def my_reduce(function, iterable, initializer=None):
    """
    Apply a function of two arguments cumulatively to the items of a sequence,
     from left to right, so as to reduce the sequence to a single value.
    If initializer is present, it is placed before the items of the sequence in the calculation,
    and serves as a default when the sequence is empty.
    For example, reduce(lambda x, y: x*y, [1, 2, 3]) calculates ((1*2)*3) return value 6
    :param_1 function
    :param_2 iterable 
    :param_3 initializer
    :type (function: (_T, _S) -> _T, sequence: Iterable[_S], initial: _T) -> _T
          (function: (_T, _T) -> _T, sequence: Iterable[_T]) -> _T
    :return value
    """
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for itm in it:
        value = function(value, itm)
    return value


my_list = [number for number in range(100, 1001) if number % 2 == 0]
print(my_reduce(lambda x, y: x * y, my_list))
