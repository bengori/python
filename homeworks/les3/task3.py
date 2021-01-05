"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает
сумму наибольших двух аргументов
"""
print('Сумма двух максимальных чисел из трех')


def my_func(x: float, y: float, z: float) -> float:
    """ My sum function. Return the sum of the largest two arguments
    :type x: float or int digit
    :type y: float or int digit
    :type z: float or int digit
    """
    my_list = [x, y, z]
    my_list = sorted(my_list)
    return my_list[-1] + my_list[1]


while True:
    user_answer = input('Введите три числа через пробел:\n>>>').split()
    try:
        num_1, num_2, num_3 = user_answer
        sum_two_max = my_func(float(num_1), float(num_2), float(num_3))
    except ValueError as e:
        print(f'Недопустимый тип данных: {e}. Необходимо ввести три числа')
    else:
        print(f'Сумма двух максимальных чисел равна {sum_two_max}')
        break
