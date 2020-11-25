"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс
«Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
(принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве
единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например
словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип
данных. Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум
возможностей, изученных на уроках по ООП.
"""
import random


class Equipment:
    # реализовала в данным классе, чтобы показать, что помню как 'защитить' список атрибутов
    __slots__ = ['name', 'producer', 'model', 'price', 'bar_code', 'group', ]

    def __init__(self, name: str, producer: str, model: str, price: int, bar_code: int):
        """
        Метод-конструктор экземпляра класса. Необходимые аргументы:
        наименование, производитель, модель, цена, штрихкод
        """
        self.name = name
        self.producer = producer
        self.model = model
        self.price = price
        self.bar_code = bar_code
        self.group = self.__class__.__name__
        if not isinstance(name, str):
            raise TypeError('Ошибка ввода данных. Необходимый тип str')
        elif not isinstance(producer, str):
            raise TypeError('Ошибка ввода данных. Необходимый тип str')
        elif not isinstance(model, str):
            raise TypeError('Ошибка ввода данных. Необходимый тип str')
        elif not isinstance(price, int):
            raise TypeError('Ошибка ввода данных. Необходимый тип int')
        elif not isinstance(bar_code, int):
            raise TypeError('Ошибка ввода данных. Необходимый тип int')
        elif len(str(bar_code)) != 13:
            raise ValueError('Ошибка ввода данных. Длина штрихкода 13 символов')

    @property
    def group_name(self):
        return self.group

    def __str__(self):
        return f'{self.name} {self.producer} {self.model} {self.price} {self.bar_code}'


class Printer(Equipment):

    def __init__(self, name, producer, model, price, bar_code, color='b/w'):
        """Метод-конструктор экземпляра класса. Необходимые аргументы:
        наименование, производитель, модель, цена, штрихкод (наследуются от родительского класса);
        количество цветов
        """
        super().__init__(name, producer, model, price, bar_code)
        self.color = color
        if self.color not in ['colored', 'black/white']:
            raise ValueError('Недопустимое значение аргумента. Может быть colored или black/white')

    # реализовала только в этом классе
    @classmethod
    def create_printer(cls, name, producer, model, price, amount):
        return [cls(name, producer, model, price, random.randint(1000000000000, 9999999999999), 'black/white') for _ in
                range(amount)]


class Scanner(Equipment):

    def __init__(self, name, producer, model, price, bar_code, resolution, format_device):
        """Метод-конструктор экземпляра класса. Необходимые аргументы:
        наименование, производитель, модель, цена, штрихкод (наследуются от родительского класса);
        формат носителя , разрешение (в ppi)
        """
        super().__init__(name, producer, model, price, bar_code)
        self.format_device = format_device
        self.resolution = resolution
        if 400 <= self.resolution <= 1200:
            raise ValueError('Недопустимое значение аргумента. Должно быть от 400 до 1200')
        elif self.format_device not in ['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6']:
            raise ValueError('Недопустимое значение аргумента. a0 - a6')


class Copier(Equipment):

    def __init__(self, name, producer, model, price, bar_code, speed: int):
        """Метод-конструктор экземпляра класса. Необходимые аргументы:
        наименование, производитель, модель, цена, штрихкод (наследуются от родительского класса);
        скорость печати
        """
        super().__init__(name, producer, model, price, bar_code)
        self.speed = speed
        if not isinstance(self.speed, int):
            raise ValueError('Недопустимое значение аргумента')
        elif self.speed >= 30:
            raise ValueError('Недопустимое значение аргумента. Должно быть менее 30')

    # реализовала только в данном классе
    @staticmethod
    def action_copy():
        return f'Копирую'


class StorageIter:

    def __init__(self, my_dict):
        self.my_dict = my_dict
        self.idx = 0

    def __next__(self):
        try:
            while True:
                equipment = self.my_dict[self.idx]
                self.idx += 1
                return equipment
        except IndexError:
            raise StopIteration


class Storage:
    __slots__ = ['_name_store', '_max_amount_obj', '_my_dict']

    def __init__(self, name_store: str, max_amount_obj=100):
        """
        Метод-конструктор экземпляра класса Склад.
        :param_1 наименование склада
        :param_2 максимльное количество объектов (по умолчанию 100 ед.)
        """
        self._name_store = name_store
        self._max_amount_obj = max_amount_obj
        self._my_dict = {}

    def __iter__(self):
        return StorageIter(self._my_dict)

    def __getitem__(self, item):
        return self._my_dict[item]

    # добавление товара на склад
    def add_to(self, equipment):
        """
        Метод добавляет в словарь объект по его названию, в значении
        будет список экземпляров этого объекта
        """
        self._my_dict.setdefault(equipment.group_name, []).append(equipment)

    # выдача товара со склада
    def extract(self, name):
        """
        Извлекаем из словаря объекта по названию группы.
        Затем извлекаем по модели, и далее по штрихкоду
        """
        if self._my_dict[name]:
            self._my_dict.setdefault(name).pop(0)
            # извлекаем по модели, и далее по штрихкоду
            pass

    # количества свободных мест на складе
    @property
    def free_volume(self):
        result = self._max_amount_obj
        for item in self._my_dict.values():
            result -= len(item)
        return result


# создаем склад
main_storage = Storage('main_storage')
# создаем партию принтеров из 10 ед
printers = Printer.create_printer('printer', 'Canon', '1028', 6000, 10)
# создаем ксерокс 1 ед.
copier = Copier('copier', 'HP', '1247', 5000, 4690761237612, 20)
# отправляем ксерокс и принтеры на склад
main_storage.add_to(copier)
for printer in printers:
    main_storage.add_to(printer)
# смотрим, что на складе
print(main_storage._my_dict)
# забираем со склада ксерокс и выводим, что на складе
main_storage.extract('Copier')
print(main_storage._my_dict)
print(main_storage.free_volume)
