from abc import ABC, abstractmethod
class Component(ABC):
    @abstractmethod
    def display(self):
        pass
class Leaf(Component):
    def __init__(self, name):
        self._name = name

    def display(self):
        print(f"Leaf {self._name}")
class Composite(Component):
    def __init__(self, name):
        self._name = name
        self._children = []

    def display(self):
        print(f"Composite {self._name}")
        for child in self._children:
            child.display()

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
composite1.display()