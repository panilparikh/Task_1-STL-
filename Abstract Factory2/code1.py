from abc import ABC, abstractmethod
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass
    @abstractmethod
    def create_sofa(self):
        pass
class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass
class Sofa(ABC):
    @abstractmethod
    def relax_on(self):
        pass