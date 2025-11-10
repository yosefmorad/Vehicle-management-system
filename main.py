from classes.electriccar import ElectricCar
from classes.Car import Car
from classes.truck import Truck
from classes.engine import Engine

# engine = Engine(12 ,"toyota")
# car_a = ElectricCar(engine ,5656 ,9)
engine = Engine(95, 1600)
car = Car(engine ,3 ,engine)
engine_electric = Engine('electric', "200")
BYD = ElectricCar("234-65-436", '2021', engine_electric)
volvo_truck = Truck('23-234-43', 2013, 5500)
vehicles = [car, BYD, volvo_truck]
for i in vehicles:
    print(i.calculate_annual_tax())
BYD.

print(BYD.charge())
print(BYD.get_luxury_features())
