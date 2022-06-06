from time import sleep


class Auto:
    def __init__(self, brand: str, age: int, color:str, mark: str):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark

    def move(self):
        print('move')

    def birthday(self):
        new_age = self.age = self.age +1
        print(new_age)

    def stop(self):
        print('stop')


class Truck(Auto):
    def __init__(self, brand: str, age: int, color:str, mark: str,max_load: int):
        Auto.__init__(self, brand,age, color, mark)
        self.max_load = max_load
    def move(self):
        print('attention')
        print('move')

    def load(self):
        sleep(1)
        print('load')
        sleep(1)

class Car(Auto):
    def __init__(self, brand: str, age: int, color:str, mark: str,max_speed: int):
        Auto.__init__(self, brand,age, color, mark)
        self.max_speed = max_speed
    def move(self):
        print('move')
        print('max_speed is <max_speed>')


truck_1 = Truck('brand1',8,'red','mark1',1)
truck_1.load()
truck_2 = Truck('brand2',8,'blue','mark2',2)
truck_2.move()

car_1 = Car('brand1',8,'red','mark1',200)
car_1.move()
