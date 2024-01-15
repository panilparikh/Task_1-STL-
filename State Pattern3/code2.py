from abc import ABC, abstractmethod
class VendingMachine:
    def __init__(self):
        self._state = NoCoinState(self)

    def set_state(self, state):
        self._state = state

    def insert_coin(self):
        self._state.insert_coin()

    def eject_coin(self):
        self._state.eject_coin()

    def dispense_item(self):
        self._state.dispense_item()
class State(ABC):
    @abstractmethod
    def insert_coin(self):
        pass

    @abstractmethod
    def eject_coin(self):
        pass

    @abstractmethod
    def dispense_item(self):
        pass
class NoCoinState(State):
    def __init__(self, vending_machine):
        self._vending_machine = vending_machine

    def insert_coin(self):
        print("Coin inserted")
        self._vending_machine.set_state(HasCoinState(self._vending_machine))

    def eject_coin(self):
        print("No coin to eject")

    def dispense_item(self):
        print("Please insert a coin")
class HasCoinState(State):
    def __init__(self, vending_machine):
        self._vending_machine = vending_machine

    def insert_coin(self):
        print("Coin already inserted")

    def eject_coin(self):
        print("Coin ejected")
        self._vending_machine.set_state(NoCoinState(self._vending_machine))

    def dispense_item(self):
        print("Item dispensed")
        self._vending_machine.set_state(NoCoinState(self._vending_machine))
vending_machine = VendingMachine()
vending_machine.dispense_item() 
vending_machine.insert_coin()   
vending_machine.dispense_item()  
vending_machine.insert_coin()    
vending_machine.eject_coin()   
vending_machine.dispense_item() 
