"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
import math
from os import path
path = path.join(path.dirname(__file__), 'task3.txt')
with open(path, 'r', encoding='utf-8') as file:
    list_employees = []
    incomes = []
    for line in file:
        surname, income = line.split()
        incomes.append(float(income))
        if float(income) < 20000:
            list_employees.append(surname)
    average_income = sum(incomes)/len(incomes)
    print(f'Список сотрудников с окладом менее 20 тыс.y.e.: {list_employees}')
    print(f'Средний доход сотрудников: {math.ceil(average_income)} y.e.')
