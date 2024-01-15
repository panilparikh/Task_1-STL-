from abc import ABC, abstractmethod
class TrafficLight:
    def __init__(self):
        self._state = None
    def set_state(self, state):
        print(f"Changing state to {type(state).__name__}")
        self._state = state
    def request(self):
        self._state.handle()