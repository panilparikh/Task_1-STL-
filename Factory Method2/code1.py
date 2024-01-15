from abc import ABC, abstractmethod
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