from classes.vehicle import Vehicle
from classes.engine import Engine
class Car(Vehicle):
    def __init__(self ,license_plate ,year,engine:Engine):
        super().__init__(license_plate  ,year)
        self.Engine = engine.horsepower

    def calculate_annual_tax(self):
        return f" 23 * {self.Engine} * 25 * year"