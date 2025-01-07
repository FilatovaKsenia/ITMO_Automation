class car:

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def starting_the_car(self):
        print('Автомобиль заведен')

    def turning_off_the_car(self):
        print('Автомобиль заглушен')

    def car_year(self):
        print(self.year)

    def car_type(self):
        print(self.type)

    def car_color(self):
        print (self.color)

Car = car('red', 'passenger car', 2005)
Car.starting_the_car()
Car.turning_off_the_car()
Car.car_year()
Car.car_type()
Car.car_color()

