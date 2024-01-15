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
class Leaf(Component):
    def __init__(self, name):
        self._name = name
    def operation(self):
        print(f"Leaf {self._name} operation")
    def add(self, component):
        print("Cannot add to a Leaf")
    def remove(self, component):
        print("Cannot remove from a Leaf")
class Composite(Component):
    def __init__(self, name):
        self._name = name
        self._children = []
    def operation(self):
        print(f"Composite {self._name} operation")
        for child in self._children:
            child.operation()
    def add(self, component):
        self._children.append(component)
    def remove(self, component):
        self._children.remove(component)
leaf1 = Leaf("A")
leaf2 = Leaf("B")
leaf3 = Leaf("C")
composite1 = Composite("X")
composite1.add(leaf1)
composite1.add(leaf2)
composite2 = Composite("Y")
composite2.add(leaf3)
composite1.add(composite2)
composite1.operation()