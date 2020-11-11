"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно,
чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий
название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб)
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
from os import path
path = path.join(path.dirname(__file__), 'task6.txt')
dict_lesson = {}
with open(path, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.replace(':', '').replace('(л)', '').replace('(лаб)', '').replace('(пр)', '').replace('—', '')
        base = line.split()
        dict_lesson[base[0]] = sum(map(int, base[1:]))
    print(dict_lesson)
