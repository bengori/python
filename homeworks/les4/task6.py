"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый
цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет
прекращено.
"""
from itertools import count, cycle


def my_iter1(start_value, end_value=float('inf'),  step=1):
    """Моя функция итератор, генерирует числа, начиная с указанного,
    с возможностью указать шаг (по умолчанию равен 1) и конечное значение списка
    (по умолчанию бесконечность)
    :param_1 start_value: число (int or float number), с которого начинается цикл
    :param_2 end_value: число (int or float number), по достижении которого цикл завершается
    :param_3 step: число (int or float number), шаг
    """
    for number in count(start_value, step):
        yield number
        if number >= end_value:
            break


def my_iter2(end_repeat=float('inf'), *args):
    """Моя функция, создающая итератор для формирования бесконечного цикла набора значения
    c возможностью выхода из цикла при указании количества повторений (по умолчанию бесконечность).
    :param_1 end_repeat: число (int number), количество повторений, при котором цикл завершается
    :param_2 args: число/строка или список, значения элементов которого повторяются
    """
    amount_repeat = 0
    for el in cycle(args):
        if amount_repeat == end_repeat:
            break
        yield el
        amount_repeat += 1


for itm in my_iter1(3, 10):
    print(itm)

for itm in my_iter1(3.45, 10.78, 1.75):
    print(itm)

my_list = [1.1, 22, 333]
for itm in my_iter2(15, *my_list):
    print(itm)

my_string = 'geekbrains'
for itm in my_iter2(14, *my_string):
    print(itm)
