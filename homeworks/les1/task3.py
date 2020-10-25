"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
код будет корректно работать, если целое положительное число
"""

while True:
    number = int(input('Введите целое положительное число (n):\n >>> '))
    if number <= 0:
        print('Надо ввести целое положительное число!')
    else:
        number1 = str(number)*2
        number1 = int(number1)
        number2 = str(number)*3
        number2 = int(number2)
        number3 = number + number1 + number2
        result = f'Сумма чисел {number} + {number1} + {number2} = {number3}'
        break

print(result)
