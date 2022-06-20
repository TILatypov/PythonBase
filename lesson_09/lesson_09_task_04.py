'''
4. Реализуйте базовый класс Car:
● у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат.
'''

print('----- Task_04 -----')


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(self.name, 'goes')

    def stop(self):
        print(self.name, 'stoped')

    def turn(self, direction):
        print((self.name).capitalize(), 'turned to', direction)

    def show_speed(self):
        print(f'Current speed of {self.color} {self.name} is {self.speed}')

class TownCar(Car):
#    print('It is a town car.')
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Maximum speed exceeded. Current speed is {self.speed}')

class SportCar(Car):
    pass
#    print('It is a sport car.')

class WorkCar(Car):
#    print('It is a lorry.')
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Maximum speed exceeded. Current speed is {self.speed}')

class PoliceCar(Car):
    pass
#    print('It is a police car.')


town_car = TownCar(80, 'black', 'car', False)
town_car.show_speed()
sport_car = SportCar(200, 'red', 'race car', False)
sport_car.show_speed()
work_car = WorkCar(40, 'orange', 'lorry', False)
work_car.show_speed()
work_car.turn('back')
police_car = PoliceCar(60, 'white', 'police car', True)
police_car.show_speed()
