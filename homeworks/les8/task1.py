"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором
@staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class MyDate:

    # в задании требовалось применить декораторы @classmethod и @staticmethod, исходя из сути методов,
    # первый извлекает дд мм гггг, второй проверяет их на корректность. Поскольку данные методы необходимы,
    # чтобы проверить корректность данных при создании экземпляра класса, показалось немного нелогичным, что функция
    # конструктор принимает дату формата "ДД-ММ-ГГГГ". Исходя из реализованного @classmethod хотелось передать
    # аргументы day, month, year  в конструктор для создания экземпляра класса Date. Поэтому мой метод
    # get_date_from_string создает экземпляр класса Date.

    def __init__(self, date_string_correct):
        self.date_string_correct = date_string_correct
        if not isinstance(date_string_correct, str):
            raise TypeError('Неверный тип данных, необходимо строковое представление даты ДД-ММ-ГГГГ')

    @classmethod
    def get_date_from_string(cls, date_string):
        """Метод извлекает из строки ДД-ММ-ГГГГ число, месяц, год
         и преобразовывает их тип к типу int. Возвращает экземпляр класса Date
         """
        try:
            day, month, year = map(int, date_string.split('-'))
        except ValueError as err:
            print(f'Ошибка ввода данных: {err}')
        else:
            date_string1 = cls(f'{day}-{month}-{year}')
            return date_string1

    @staticmethod
    def validation_date(date_string):
        """
        Метод производит простейшую проверку аргуметов day, month,
        year на вхождение в допустимый диапозон. Возвращает True|False
        """
        # не реализовывала проверку на корректность количества дней в месяце
        day, month, year = map(int, date_string.split('-'))
        return 1 <= day <= 31 and 1 <= month <= 12 and 0 <= year <= 9999


if __name__ == '__main__':
    print(MyDate.validation_date('12-12-1930'))  # проверка на корректность
    print(MyDate.get_date_from_string('12-12-1930'))  # извлечение аргументов и создание экземпляра класса
    print(MyDate.validation_date('48-10-1930'))
    print(MyDate.validation_date('10-14-202'))

    try:
        MyDate.get_date_from_string('gfg-12-1930')
    except ValueError as e:
        print(f'Ошибка ввода данных {e}')

    try:
        MyDate.get_date_from_string('gfg-12-1930')
    except ValueError as e:
        print(f'Ошибка ввода данных {e}')
