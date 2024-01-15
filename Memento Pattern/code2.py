class Memento:
    def __init__(self, state):
        self._state = state
    def get_state(self):
        return self._state
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
class Caretaker:
    def __init__(self):
        self._mementos = []
    def add_memento(self, memento):
        self._mementos.append(memento)
    def get_memento(self, index):
        return self._mementos[index]
originator = Originator()
caretaker = Caretaker()
originator.set_state("State 1")
memento1 = originator.save_state_to_memento()
caretaker.add_memento(memento1)
originator.set_state("State 2")
memento2 = originator.save_state_to_memento()
caretaker.add_memento(memento2)
originator.restore_state_from_memento(caretaker.get_memento(0))