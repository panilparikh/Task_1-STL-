from abc import ABC, abstractmethod
class Component(ABC):
    @abstractmethod
    def display(self):
        pass