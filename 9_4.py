from random import choice


class Car:
    direction = ['едет прямо', 'повернула направо', 'повернула налево', 'сделала разворот']

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        if is_police == True:
            print(f'Машина: {name}, цвет: {color}.\nЭто машина полиции? Да!')
        else:
            print(f'Машина: {name}, цвет: {color}.\nЭто машина полиции? Нет!')

    def go(self):
        print(f'{self.name}: машина поехала')

    def stop(self):
        print(f'{self.name}: машина остановилась')

    def turn(self):
        print(f'{self.name}: машина {choice(self.direction)}')

    def show_speed(self):
        return f'{self.name}: скорость машины {self.speed} км/ч'


class TownCar(Car):
    def show_speed(self):
        return f'{self.name}: скорость машины: {self.speed} км/ч. Превышение скорости!' if self.speed > 60 else super().show_speed()


class WorkCar(Car):
    def show_speed(self):
        return f'{self.name}: скорость машины: {self.speed} км/ч. Превышение скорости!' if self.speed > 40 else super().show_speed()


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, is_police=True)


police_car = PoliceCar('"LADA Largus"', 'белый', 80)
work_car = WorkCar('"FORD Transit"', 'серый', 60)
sport_car = SportCar('"Chevrolet Corvette"', 'черный', 120)
town_car = TownCar('"KIA Ceed"', 'синий', 70)

list_car = [police_car, work_car, sport_car, town_car]

for i in list_car:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()
