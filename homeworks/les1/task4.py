"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

while True:
    number = input('Введите целое положительное число (n):\n >>> ')
    if int(number) <= 0:
        print('Надо ввести целое положительное число!')
    else:
        number = list(number)
        max_number = number[0]
        for number in number:
            if number > max_number:
                max_number = number
        print(f'Максимальная цифра в числе - {max_number}')
        break
