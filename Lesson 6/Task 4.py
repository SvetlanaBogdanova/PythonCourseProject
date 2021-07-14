class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала!')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')


class TownCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Превышение скорости на {self.speed - 60} км/час!')


class WorkCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Превышение скорости на {self.speed - 40} км/час!')


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


my_car_1 = TownCar(65, 'red', 'Lexus')
print(f'Автомобиль {my_car_1.name}, цвет {my_car_1.color}')
my_car_1.go()
my_car_1.turn('налево')
my_car_1.show_speed()
print()

my_car_2 = WorkCar(45, 'gray', 'Ford')
print(f'Автомобиль {my_car_2.name}, цвет {my_car_2.color}')
my_car_2.show_speed()
my_car_2.stop()
print()

my_car_3 = SportCar(150, 'red', 'Ferrari')
print(f'Автомобиль {my_car_3.name}, цвет {my_car_3.color}')
my_car_3.show_speed()
print()

my_car_4 = PoliceCar(75, 'black', 'Toyota')
print(f'Автомобиль {my_car_4.name}, цвет {my_car_4.color}')
my_car_4.show_speed()
