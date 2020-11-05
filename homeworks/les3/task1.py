"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""
print('Деление двух чисел')


def division(num_1: float, num_2: float) -> float:
    """ Return the quotient of the division two numbers.
    :type num_1: float or int number
    :type num_2: float or int number
    """
    try:
        return num_1 / num_2
    except ZeroDivisionError as error:
        print(f'Ошибка: {error}. Деление на ноль')
        return float('nan')


#  альтернативный вариант записи функции через lambda-функцию
#  division2 = lambda dividend, divider: dividend / divider

while True:
    try:
        user_answer = input('Введите делимое и делитель через запятую:\n>>>').split(',')
        dividend, divider = user_answer
        quotient = division(float(dividend), float(divider))
    except ValueError as e:
        print(f'Введены некорректные данные: {e}')
    else:
        print(f'{dividend}/{divider} = {quotient}')
        break
