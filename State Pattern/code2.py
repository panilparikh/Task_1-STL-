from abc import ABC, abstractmethod
class Context:
    def __init__(self, initial_state):
        self._state = initial_state
    def set_state(self, new_state):
        print(f"Changing state to {type(new_state).__name__}")
        self._state = new_state
    def request(self):
        self._state.handle()
class State(ABC):
    @abstractmethod
    def handle(self):
        pass
class StateA(State):
    def handle(self):
        print("Handling request in StateA")
class StateB(State):
    def handle(self):
        print("Handling request in StateB")
context = Context(StateA())  
context.request()  
context.set_state(StateB())  
context.request() 