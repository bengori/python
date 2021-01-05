"""
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from os import path
from random import randint
path = path.join(path.dirname(__file__), 'task5.txt')
with open(path, 'w', encoding='utf-8') as file:
    numbers_list = ' '.join([str(randint(1, 100)) for i in range(1, 10)])
    print(numbers_list)  # для проверки работы кода
    file.write(numbers_list)

with open(path, 'r', encoding='utf-8') as file:
    for line in file:
        numbers = line.split(' ')
    print(sum(map(int, numbers)))
