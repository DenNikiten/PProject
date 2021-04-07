
1.
# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep

class TrafficLight:
    __color = "None"

    def running(self):
        while True:
            print("Trafficlight is Red right now")
            sleep(7)
            print("Trafficlight is Yellow right now")
            sleep(2)
            print("Trafficlight is Green right now")
            sleep(9)
            print("Trafficlight is Yellow right now")
            sleep(2)

traffic_light = TrafficLight()
traffic_light.running()

2.
# Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны передаваться
# при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги
# асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight_asphalt(self, weight, thickness):
        return f"{int((self._length * self._width * weight * thickness) / 1000)} т"

road_1 = Road(20, 5000)
s = road_1.weight_asphalt(25, 5)
print(s)

3.
# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return f"{sum(self._income.values())} {'$'}"

specialist = Position("Denis", "Nikitenko", "Lead", 1000000, 600000)
print(specialist.get_full_name())
print(specialist.position)
print(specialist.get_total_income())

4.
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость
# автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
# о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def __str__(self):
        return f"Скорость: {self.speed}, цвет: {self.color}, марка: {self.name}, полиция: {self.is_police}"

    def show_speed(self):
        return f"Скорость автомобиля {self.name} {self.speed}."

    def go(self):
        print(f"Машина {self.name} поехала.")

    def stop(self):
        print(f"Машина {self.name} остановилась.")

    def turn(self, direction):
        print(f"Машина {self.name} повернула {"налево" if direction == 0 else "направо"}.")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Скорость {self.name} выше 60 км.ч. и составляет {self.speed} км.ч. Скорость превышена!")

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Скорость {self.name} выше 40 км.ч. и составляет {self.speed} км.ч. Скорость превышена!")

class PoliceCar(Car):
    ''' Полицейский автомобиль '''

class SportCar(Car):
    ''' Спортивный автомобиль'''

town_car = TownCar(86, "Black", "Maserati", False)
print(town_car)
town_car.go()
town_car.show_speed()
town_car.turn(0)
town_car.stop()
print()

work_car = WorkCar(51, "Brown", "Mazda", False)
print(work_car)
work_car.go()
work_car.show_speed()
work_car.turn(8)
work_car.stop()
print()

police_car = PoliceCar(100, "Blue", "Porsche", True)
print(police_car)
police_car.go()
print(police_car.show_speed())
police_car.turn(10)
police_car.stop()
print()

5.
# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод
# для каждого экземпляра.

class Stationery:
    title = "Blackberry"

    def draw(self):
        print(f"{Stationery.title}: Запуск отрисовки.")

class Pen(Stationery):
    def draw(self):
        return "Ручка не пишет!"

class Pencil(Stationery):
    def draw(self):
        return "Карандаш сломался!"

class Handle(Stationery):
    def draw(self):
        return "Маркер очень жирно рисует!"

stationery = Stationery()
stationery.draw()
pen = Pen()
print(pen.draw())
pencil = Pencil()
print(pencil.draw())
handle = Handle()
print(handle.draw())
