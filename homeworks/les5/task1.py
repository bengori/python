"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые
пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""
from os import path
path = path.join(path.dirname(__file__), 'task1.txt')
with open(path, 'w', encoding='utf-8') as file:
    print('Введите текст, который хотите записать в файл')
    while True:
        str_text = input('>>>')
        if not str_text:
            break
        else:
            file.write(f'{str_text}\n')
