"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def my_map(func, iter_obj):
    result = [func(el) for el in iter_obj]
    return result


def int_func(text: str) -> str:
    """My func: return 'word'->'Word'
    """
    new_word = text.title()
    return new_word


def int_func2(text: str) -> str:
    """My func: return 'hello world'->'Hello World'"""
    text = text.split()
    new_string = my_map(int_func, text)
    new_string = ' '.join(new_string)
    return new_string


word = int_func('test')
print(word)
string = int_func2('hello world')
print(string)
