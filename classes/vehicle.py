from abc import ABC ,abstractmethod
class Vehicle(ABC):
    def __init__(self  ,license_plate ,year):
        self.__license_plate = license_plate
        self.__year = year



    def get_license_plate(self):
        if self.__license_plate:
            return f"license_plate :{self.__license_plate}"
        return "its no good"


    def set_license_plate(self ,new):
        if new:
            self.__license_plate = new


    def get_year(self):
        return f" year :{self.__year}"

    def set_year(self ,new_year):
        if new_year:
            self.__year = new_year

    @abstractmethod
    def calculate_annual_tax(self):
        pass
