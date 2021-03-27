from random import random


class Car:
    __directions = {'left', 'right'}
    _is_police = False

    def __init__(self, name, color, speed=0):
        self.name = name
        self.color = color
        self.speed = speed

    def go(self, speed=int(random() * 100)):
        if not speed > 0:
            print(f'Ошибка! неверная скорость {speed}')
        if self.speed == 0:
            print(f'Машина поехала со скоростью {speed} км/ч')
        elif self.speed == speed:
            print(f'Машина и так двигается со скоростью {speed} км/ч')
        else:
            print(f'Машина изменила скорость на {speed} км/ч')
        self.speed = speed

    def stop(self):
        if self.speed == 0:
            print('Машина и так стоит')
        else:
            print('Машина остановилась')
            self.speed = 0

    def turn(self, direction):
        if not direction.lower() in self.__directions:
            print('Wrong direction')
            return 1
        print(f'The car turned {direction.lower()}')

    def show_speed(self):
        print(f'Скорость машины: {self.speed}')

    def is_police(self):
        return self._is_police


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Вы превысили скорость на {self.speed - 60}')
        else:
            super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Вы превысили скорость на {self.speed - 40}')
        else:
            super().show_speed()


class PoliceCar(Car):
    _is_police = True


car1 = PoliceCar('passat', 'green')
car1.show_speed()
car1.go()
car1.show_speed()
car1.go(100)
car1.stop()
car1.turn('right')
car1.stop()
print(car1.is_police())
