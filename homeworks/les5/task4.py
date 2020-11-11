"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
 При этом английские числительные должны заменяться на русские.
 Новый блок строк должен записываться в новый текстовый файл.
 """
from os import path
path = path.join(path.dirname(__file__), 'task4.txt')
dict_number = {
    'One': 'один',
    'Two': 'два',
    'Three': 'три',
    'Four': 'четыре',
}

with open(path, 'r', encoding='utf-8') as file:
    new_text = []
    for line in file:
        line = line.replace('—', '')
        text_number, digit = line.split()
        new_line = f'{dict_number[text_number]} — {digit}\n'
        new_text.append(new_line)
    new_text[-1] = new_text[-1].rstrip('\n')  # чтобы не было пустой строки в файле

with open('task4_2.txt', 'w', encoding='utf-8') as file:  # альтернативный вариант открыть файл на дозапись режим 'a'
    file.writelines(new_text)
