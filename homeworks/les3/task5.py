"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
к полученной ранее сумме и после этого завершить программу.
"""
print('Сумма чисел')


def my_sum(*args):
    """Return sum of sequence elements
    :type args float or int number
    """
    elm_sum = 0
    for arg in args:
        try:
            elm_sum += float(arg)
        except ValueError as e:
            print(f'Недопустимый тип данных {e}')
            break
    return elm_sum


total_sum = 0
start_sum = 0
while True:
    user_answer = input('Введите числа через пробел:\n>>>').split()
    elm_list = user_answer
    start_sum = my_sum(*elm_list)
    total_sum += start_sum
    print(total_sum)
