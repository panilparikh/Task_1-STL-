from abc import ABC, abstractmethod
class TrafficLight:
    def __init__(self):
        self._state = None
    def set_state(self, state):
        print(f"Changing state to {type(state).__name__}")
        self._state = state
    def request(self):
        self._state.handle()
class State(ABC):
    @abstractmethod
    def handle(self):
        pass
class RedState(State):
    def handle(self):
        print("Traffic Light: Red")
class YellowState(State):
    def handle(self):
        print("Traffic Light: Yellow")
class GreenState(State):
    def handle(self):
        print("Traffic Light: Green")
traffic_light = TrafficLight()
red_state = RedState()
yellow_state = YellowState()
green_state = GreenState()
traffic_light.set_state(red_state)
traffic_light.request()  
traffic_light.set_state(yellow_state)
traffic_light.request() 
traffic_light.set_state(green_state)
traffic_light.request()  