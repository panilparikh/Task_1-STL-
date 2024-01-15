from abc import ABC, abstractmethod
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass
    @abstractmethod
    def next(self):
        pass
class CustomIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._index = 0
    def has_next(self):
        return self._index < len(self._collection)
    def next(self):
        if self.has_next():
            value = self._collection[self._index]
            self._index += 1
            return value
        else:
            raise StopIteration("No more elements in the collection")
class CustomCollection:
    def __init__(self):
        self._elements = []
    def add_element(self, element):
        self._elements.append(element)
    def create_iterator(self):
        return CustomIterator(self._elements)
custom_collection = CustomCollection()
custom_collection.add_element("Element 1")
custom_collection.add_element("Element 2")
custom_collection.add_element("Element 3")
iterator = custom_collection.create_iterator()
while iterator.has_next():
    print(iterator.next())
