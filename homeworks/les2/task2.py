"""
Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
print('Давайте создадим список дней недели')
while True:
    user_answer = input('Введите дни недели через пробел или запятую:\n>>>').lower()
    user_list = user_answer.replace(',', ' ').split()
    # перечень дней недели
    weekdays = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
    # проверка: входят ли ответы пользователя в список дней недели, если да результат проверки 1, нет - 0
    correct_input = [1 if i in weekdays else 0 for i in user_list]
    # обработка исключения - ошибки ввода, когда в списке correct_input есть 0, значит данные введены некорректно
    try:
        for element in correct_input:
            if element == 0:
                raise ValueError('такого дня(дней) недели нет')
    except ValueError as error:
        print('Ошибка ввода:', error)
    else:
        count_elements = len(user_list) - 1
        index = 0
        while index < count_elements:
            user_list[index], user_list[index + 1] = user_list[index + 1], user_list[index]
            index += 2
        print(user_list)
        break
