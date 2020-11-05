"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры
как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""
print('Вывод информации о пользователе')


def user_info(**kwargs):
    """Return some information about the user in one string"""
    result = [f'{key}: {value}' for key, value in kwargs.items()]
    return print(f'Информация о пользователе: {result}')


user_template = {
    'name': ('Введите имя пользователя:\n>>>', str),
    'surname': ('Введите фамилию пользователя:\n>>>', str),
    'year': ('Введите год рождения:\n>>>', int),
    'city': ('Введите город проживания:\n>>>', str),
    'email': ('Введите email пользователя\n>>>', str),
    'phone': ('Введите телефон пользователя\n>>>', str),
}

for key, value in user_template.items():
    while True:
        user_answer = input(f'{value[0]}')
        try:
            user_answer = value[1](user_answer)
        except ValueError as error:
            print(f'Неверный тип данных: {error}')
            continue
        user_template[key] = user_answer
        break

user_info(**user_template)
