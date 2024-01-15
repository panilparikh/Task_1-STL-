from abc import ABC, abstractmethod
class Component(ABC):
    @abstractmethod
    def operation(self):
        pass
    @abstractmethod
    def add(self, component):
        pass
    @abstractmethod
    def remove(self, component):
        pass