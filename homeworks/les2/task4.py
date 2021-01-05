""" Пользователь вводит строку из нескольких слов, разделённых пробелами.
 Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
 Если в слово длинное, выводить только первые 10 букв в слове.
 """
while True:
    try:
        user_answer = input('Введите строку из нескольких слов разделенных пробелами:\n>>>')
        if len(user_answer) <= 5:
            raise ValueError()
        if user_answer.isspace():
            raise ValueError()
    except ValueError as error:
        print('Введите более длинную строку')
    else:
        for ind, el in enumerate(user_answer.split(), 1):
            print(ind, el[:10])
        break
