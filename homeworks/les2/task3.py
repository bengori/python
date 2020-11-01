"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и через dict.
"""
dict_season = {
    1: 'зима',
    2: 'зима',
    3: 'весна',
    4: 'весна',
    5: 'весна',
    6: 'лето',
    7: 'лето',
    8: 'лето',
    9: 'осень',
    10: 'осень',
    11: 'осень',
    12: 'зима',
}

list_season = ['зима', 'весна', 'лето', 'осень']

while True:
    try:
        user_answer = int(input('Введите номер месяца в виде целого числа от 1 до 12\n>>>'))
        if user_answer < 0 or user_answer > 12:
            raise ValueError()
    except ValueError as error:
        print('Некорректные данные. Необходимо ввести целое число от 1 до 12')
    else:
        print('Сезон года (решение через dict):', dict_season[user_answer])
        index_list_season = user_answer//3 - 4
        print('Сезон года (решение через list):', list_season[index_list_season])
        break
