from classes.vehicle import Vehicle
from classes.engine import Engine
class Truck(Vehicle):
    def __init__(self ,license_plate ,year ,max_load):
        super().__init__(license_plate ,year)
        self.max_load =max_load

    def calculate_annual_tax(self):
        return 12 *  self.max_load
