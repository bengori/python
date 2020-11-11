"""Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет
 количества строк, количества слов в каждой строке.
 """
from os import path
path = path.join(path.dirname(__file__), 'task2.txt')
with open(path, 'r', encoding='utf-8') as file:
    content = file.readlines()
    print(f'Количество строк в файле: {len(content)}')

with open(path, 'r', encoding='utf-8') as file:
    for ind, line in enumerate(file, 1):
        #  replace применила с учетом того, что может потребоваться посчитать уникальные слова
        #  в нашем случае применение replace не влияет на результат
        line = line.replace('\n', '').replace(',', '').replace('.', '').replace('"', '')
        line = line.replace('!', '').replace(';', '').replace(':', '').replace('?', '')
        words_amount = len(line.split())
        print(f'Строка {ind}: количество слов {words_amount}')
