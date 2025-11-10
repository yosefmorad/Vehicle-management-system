from classes.electricMixin import ElectricMixin
from classes.Car import Car
from classes.luxuryMixin import LuxuryMixin

class ElectricCar(ElectricMixin,LuxuryMixin,Car):
    def calculate_annual_tax(self):
        return f'the tax for electric car is 250 usd$'