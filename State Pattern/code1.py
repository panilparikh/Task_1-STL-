from abc import ABC, abstractmethod
class Context:
    def __init__(self, initial_state):
        self._state = initial_state
    def set_state(self, new_state):
        print(f"Changing state to {type(new_state).__name__}")
        self._state = new_state
    def request(self):
        self._state.handle()