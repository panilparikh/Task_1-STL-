from abc import ABC, abstractmethod
class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass
class ModernChair(Chair):
    def sit_on(self):
        return "Sitting on a Modern Chair"
class VictorianChair(Chair):
    def sit_on(self):
        return "Sitting on a Victorian Chair"
class Sofa(ABC):
    @abstractmethod
    def relax_on(self):
        pass
class ModernSofa(Sofa):
    def relax_on(self):
        return "Relaxing on a Modern Sofa"
class VictorianSofa(Sofa):
    def relax_on(self):
        return "Relaxing on a Victorian Sofa"
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass
    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()
    def create_sofa(self) -> Sofa:
        return ModernSofa()
class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()
    def create_sofa(self) -> Sofa:
        return VictorianSofa()
def create_furniture(factory: FurnitureFactory):
    chair = factory.create_chair()
    sofa = factory.create_sofa()
    print(chair.sit_on())
    print(sofa.relax_on())
print("Creating Modern Furniture:")
modern_factory = ModernFurnitureFactory()
create_furniture(modern_factory)
print("\nCreating Victorian Furniture:")
victorian_factory = VictorianFurnitureFactory()
create_furniture(victorian_factory)