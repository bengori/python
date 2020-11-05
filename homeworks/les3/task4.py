"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции
my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа
в степень. Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень
с помощью оператора **. Второй — более сложная реализация без оператора **, предусматривающая
использование цикла.
"""
print('Возведение числа x в степень y')

my_func1 = lambda x, y: x ** y


def my_func2(x: float, y: int) -> float:
    """My function: return x**y(x to the power of y).
    :type x: float positive number
    :type y: int negative number
    """
    y = (-y)
    new_x = x
    for i in range(y - 1):
        new_x *= x
    total = 1 / new_x
    return total


while True:
    user_answer_1 = input('Введите действительное положительное число x:\n>>>')
    try:
        number_x = float(user_answer_1)
        if number_x <= 0:
            raise ValueError('Число должно быть положительным.')
    except ValueError as e:
        print(f'Недопустимый тип данных: {e}')
        continue
    break

while True:
    user_answer_2 = input('Введите целое отрицательное число y:\n>>>')
    try:
        number_y = int(user_answer_2)
        if number_y >= 0:
            raise ValueError('Число должно быть отрицательным.')
    except ValueError as e:
        print(f'Недопустимый тип данных: {e}')
        continue
    break

print(f'{number_x}^({number_y}) = {my_func1(number_x, number_y)} (c использованием **)')
result = my_func2(number_x, number_y)
print(f'{number_x}^({number_y}) = {result} (c использованием цикла for)')
