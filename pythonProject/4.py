# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        self.speed += 20
        print(f'начало движения')

    def stop(self):
        print(f'отсановка')

    def turning(self, direction):
        print(f'поворот на {direction}')

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed <= 60:
            print(f'Скорость автомобиля {self.speed}')
        else:
            print(f'Вы превышаете скорсть , скорость состовляет{self.speed}')


class WorkCar(Car):
    def show_speed(self):
        if self.speed <= 40:
            print(f'Скорость автомобиля {self.speed}')
        else:
            print(f'Вы превышаете скорсть , скорость состовляет{self.speed}')


class PoliceCar(Car):
    pass


class SportCar(Car):
    pass


twn_car = TownCar(80, 'Red', 'Nissan')
twn_car.show_speed()
plc_car = PoliceCar(0, 'Police', 'Porshe', is_police=True)
wrk_car = WorkCar(20, 'Yelow', 'Maz')
wrk_car.turning('лево')
