"""
Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки
типа данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно
не запрашивать у пользователя, а указать явно, в программе.
"""

my_list = [False, 567, 'happy', 4.67, (345, 'sun'), None, [1, 3, 5], {'name', 'surname'}, {'name': 'Max', 'age': 39}]

for element in my_list:
    print(type(element))
