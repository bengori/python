"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv


print('Расчет заработной платы сотрудника')


def basic_wage(output, rate, bonus):
    """ Функция расчета заработной платы сотрудника
    :param выработка в часах float
    :param ставка в час float
    :param премия float
    """
    try:
        result = float(output) * float(rate) + float(bonus)
        return print(f'Зарплата сотрудника составит {result} у.е.')
    except ValueError as e:
        print(f'Недопустимый тип данных: {e}')
        return print(f'Зарплата сотрудника: ', float('nan'))


try:
    _, output, rate, bonus, *_ = argv
except ValueError as e:
    print(f'Недостаточное количество аргументов:{e}')
    print('Необходимо указать выработку в часах, ставку в час и размер премии')
else:
    func_result = basic_wage(output, rate, bonus)
