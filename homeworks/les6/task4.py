"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении
 скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите
 результат. Выполните вызов методов и также покажите результат.
"""
import random


class Car:

    def __init__(self, name, color, is_police=False):
        self.name = name
        self.color = color
        self.speed = random.randint(0, 180)
        self.is_police = is_police

    def car_go(self):
        print('Машина поехала')

    def car_stop(self):
        print('Машина остановилась')

    def car_turn(self, turn):
        if turn in ('направо', 'налево'):
            print(f'Машина поворачивает {turn}')
        else:
            raise ValueError('Недопустимое значение. Выберите left or right')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):

    def __init__(self, name, color):
        super().__init__(name, color, False)

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости 60 км/ч')
        super().show_speed()


class SportCar(Car):

    def __init__(self, name, color):
        super().__init__(name, color, False)


class WorkCar(Car):

    def __init__(self, name, color):
        super().__init__(name, color, False)

    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости 40 км/ч')
        super().show_speed()


class PoliceCar(Car):

    def __init__(self, name, color):
        super().__init__(name, color, True)


if __name__ == '__main__':
    auto_1 = Car('BMW', 'black')
    auto_1.show_speed()
    print(auto_1.name)
    print(auto_1.is_police)
    auto_1.car_go()
    auto_1.car_stop()
    auto_1.car_turn('налево')

    auto_2 = TownCar('Mazda', 'blue')
    auto_2.show_speed()
    print(auto_2.name)
    print(auto_2.is_police)
    auto_2.car_go()
    auto_2.car_stop()
    auto_2.car_turn('направо')

    auto_3 = WorkCar('Volvo', 'grey')
    auto_3.show_speed()
    print(auto_3.color)
    print(auto_3.name)
    auto_3.car_go()
    auto_3.car_stop()
    auto_3.car_turn('налево')

    auto_4 = SportCar('Ferrari', 'green')
    auto_4.show_speed()

    auto_5 = PoliceCar('Ford', 'black and white')
    auto_5.show_speed()
    print(auto_5.is_police)
    auto_3.car_turn('прямо')
