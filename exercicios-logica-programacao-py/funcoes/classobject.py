class Car:
    def __init__(self, car, year):
        self.car = car
        self.year = year

    def age(self):
        idade = 2025 - int(self.year)
        return idade