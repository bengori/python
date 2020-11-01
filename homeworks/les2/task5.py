"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""
print('"Рейтинг"')
my_list = [34, 18, 6, 4, 4, 3, 2]
print('Список рейтингов: ', my_list)
start_program = True

while start_program:

    try:
        user_answer = int(input('Введите натуральное число:\n>>>'))
        if user_answer == 0 or user_answer < 0:
            raise ValueError()
    except ValueError as error:
        print('Необходимо ввести целое положительное число!')
    else:
        count_el = my_list.count(user_answer)
        if user_answer > my_list[0]:
            my_list.insert(0, user_answer)
        elif user_answer <= my_list[-1]:
            my_list.append(user_answer)
        # если элемента в списке нет (и элемент не max/min)
        elif count_el == 0:
            # список элементов "рейтинга", которые больше нового элемента
            part_my_list = [my_list.index(i) for i in my_list if user_answer < i]
            # индекс нового элемента - длина части списка
            index_new_el = len(part_my_list)
            my_list.insert(index_new_el, user_answer)
        # если несколько одинаковых элементов
        # определяем первую позицию элемента в списке и с учетом кол-ва одинаковых элементов вычисляем позицию нового
        else:
            index_el = my_list.index(user_answer)
            index_new_el = index_el + count_el
            my_list.insert(index_new_el, user_answer)
        print(my_list)

        while True:
            user_answer = input('Продолжим?(да/нет)\n>>>')
            if user_answer.lower() in ('да', 'нет'):
                start_program = user_answer == 'да'
                break
            else:
                print('Надо ответить да или нет')
