from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def refuel(self):
        pass

class Car(Vehicle):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
        self.air_conditioners_consumption = 0.9

    # def drive(self, distance):
    #     available_km = self.fuel_quantity / (self.fuel_consumption + self.air_conditioners_consumption)
    #     if distance <= available_km:
    #         available_km -= distance
    #         self.fuel_quantity = available_km * (self.fuel_consumption + self.air_conditioners_consumption)

    def drive(self, distance):
        liters_needed = distance * (self.fuel_consumption + self.air_conditioners_consumption)
        if liters_needed <= self.fuel_quantity:
            self.fuel_quantity -= liters_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel

class Truck(Vehicle):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
        self.air_conditioners_consumption = 1.6

    def drive(self, distance):
        liters_needed = distance * (self.fuel_consumption + self.air_conditioners_consumption)
        if liters_needed <= self.fuel_quantity:
            self.fuel_quantity -= liters_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95



car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

