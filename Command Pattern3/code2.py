from abc import ABC, abstractmethod
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
class Light:
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")
class TurnOnLightsCommand(Command):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_on()
class TurnOffLightsCommand(Command):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_off()
class AirConditioner:
    def turn_on(self):
        print("AC is ON")

    def turn_off(self):
        print("AC is OFF")
class TurnOnACCommand(Command):
    def __init__(self, ac):
        self._ac = ac

    def execute(self):
        self._ac.turn_on()
class TurnOffACCommand(Command):
    def __init__(self, ac):
        self._ac = ac

    def execute(self):
        self._ac.turn_off()
class RemoteControl:
    def __init__(self):
        self._command = None

    def set_command(self, command):
        self._command = command

    def press_button(self):
        self._command.execute()
light = Light()
ac = AirConditioner()
turn_on_lights_command = TurnOnLightsCommand(light)
turn_off_lights_command = TurnOffLightsCommand(light)
turn_on_ac_command = TurnOnACCommand(ac)
turn_off_ac_command = TurnOffACCommand(ac)
remote_control = RemoteControl()
remote_control.set_command(turn_on_lights_command)
remote_control.press_button()
remote_control.set_command(turn_off_lights_command)
remote_control.press_button()
remote_control.set_command(turn_on_ac_command)
remote_control.press_button()
remote_control.set_command(turn_off_ac_command)
remote_control.press_button() 