class Person:
    def __init__(self, fullname: str):
        self.fullname = fullname

    def __str__(self):
        return self.fullname

    def to_string(self):
        print(self.__str__())


class Driver(Person):
    def __init__(self, fullname: str, experience: int):
        super().__init__(fullname)
        self.experience = experience

    def __str__(self):
        return f'Водитель: {self.fullname}, Стаж вождения: {self.experience}'


class Engine:
    def __init__(self, power: int, company: str):
        self.power = power
        self.company = company

    def __str__(self):
        return f'Мотор: {self.power} л.с., {self.company}'

    def to_string(self):
        print(self.__str__())


class Car:
    def __init__(self, mark: str, engine: Engine, driver: Driver, car_class: str, weight: int):
        self.mark = mark
        self.engine = engine
        self.driver = driver
        self.car_class = car_class
        self.weight = weight

    def __str__(self):
        return f'Марка: {self.mark}, Класс: {self.car_class}, Вес: {self.weight}, {self.driver}, {self.engine}'

    def to_string(self):
        print(self.__str__())

    def start(self):
        print('Поехали')

    def stop(self):
        print('Останавливаемся')

    def turn_left(self):
        print('Поворот налево')

    def turn_right(self):
        print('Поворот направо')


class Lorry(Car):
    def __init__(self, mark: str, engine: Engine, driver: Driver, car_class: str, weight: int, carrying: int):
        super().__init__(mark, engine, driver, car_class, weight)
        self.carrying = carrying

    def __str__(self):
        return f"Информация о грузовике:\nМарка: {self.mark}, Класс: {self.car_class}, Вес: {self.weight}, {self.driver}, {self.engine}, Грузоподъемность: {self.carrying} кг"


class SportCar(Car):
    def __init__(self, mark: str, engine: Engine, driver: Driver, car_class: str, weight: int, speed: int):
        super().__init__(mark, engine, driver, car_class, weight)
        self.speed = speed

    def __str__(self):
        return f"Информация о спорткаре:\nМарка: {self.mark}, Класс: {self.car_class}, Вес: {self.weight}, {self.driver}, {self.engine}, Предельная скорость: {self.speed} км/ч"


toyota_engine = Engine(200, 'Toyota')
volvo_engine = Engine(300, 'Volvo')
ferrari_engine = Engine(400, 'Ferrari')

driver1 = Driver('Иван Иванов', 5)
driver2 = Driver('Петр Петров', 10)
driver3 = Driver('Анна Сидорова', 3)

car = Car('Toyota Camry', toyota_engine, driver1, 'Седан', 1500)
lorry = Lorry('Volvo FH', volvo_engine, driver2, 'Грузовик', 8000, 5000)
sport_car = SportCar('Ferrari 488', ferrari_engine, driver3, 'Спорткар', 1500, 300)

car.to_string()
lorry.to_string()
sport_car.to_string()
