class Originator:
    def __init__(self):
        self._state = None
    def set_state(self, state):
        print(f"Setting state to: {state}")
        self._state = state
    def save_state_to_memento(self):
        return Memento(self._state)
    def restore_state_from_memento(self, memento):
        self._state = memento.get_state()
        print(f"Restored state to: {self._state}")