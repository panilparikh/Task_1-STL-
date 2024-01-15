from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass
class Car(Vehicle):
    def drive(self):
        return "Driving a Car"
class Truck(Vehicle):
    def drive(self):
        return "Driving a Truck"
class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass
class CarFactory(VehicleFactory):
    def create_vehicle(self):
        return Car()
class TruckFactory(VehicleFactory):
    def create_vehicle(self):
        return Truck()
car_factory = CarFactory()
car = car_factory.create_vehicle()
print(car.drive())
truck_factory = TruckFactory()
truck = truck_factory.create_vehicle()
print(truck.drive())