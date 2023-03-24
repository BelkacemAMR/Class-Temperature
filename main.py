class Temperature:
    def __init__(self):
        self.temp = 0

    def celsius_getter(self):
        return self.temp

    def kelvin_getter(self):
        return self.temp + 273.15

    def fahrenheit_getter(self):
        return self.temp * 9 / 5 + 32

    def celsius_setter(self, value):
        self.temp = value

    def kelvin_setter(self, value):
        self.temp = value - 273.15

    def fahrenheit_setter(self, value):
        self.temp = (value - 32) * 5 / 9

    celsius = property(celsius_getter, celsius_setter)
    kelvin = property(kelvin_getter, kelvin_setter)
    fahrenheit = property(fahrenheit_getter, fahrenheit_setter)