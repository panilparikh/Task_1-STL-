from abc import ABC, abstractmethod
class StockSubject:
    def __init__(self, symbol, price):
        self._symbol = symbol
        self._price = price
        self._observers = []
    def add_observer(self, observer):
        self._observers.append(observer)
    def remove_observer(self, observer):
        self._observers.remove(observer)
    def set_price(self, price):
        self._price = price
        self.notify_observers()
    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._symbol, self._price)
class Observer(ABC):
    @abstractmethod
    def update(self, symbol, price):
        pass
class StockObserver(Observer):
    def __init__(self, name):
        self._name = name
    def update(self, symbol, price):
        print(f"{self._name} received update: {symbol} : {price}Rs")
stock = StockSubject("ABC", 100)
observer1 = StockObserver("Observer 1")
observer2 = StockObserver("Observer 2")
stock.add_observer(observer1)
stock.add_observer(observer2)
stock.set_price(105)
stock.set_price(98)