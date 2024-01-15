class Command:
    def execute(self):
        pass
# Concrete Command
class LightOnCommand(Command):
    def __init__(self, light):
        self._light = light
    def execute(self):
        self._light.turn_on()
class LightOffCommand(Command):
    def __init__(self, light):
        self._light = light
    def execute(self):
        self._light.turn_off()
# Receiver
class Light:
    def turn_on(self):
        print("Light is ON")
    def turn_off(self):
        print("Light is OFF")
# Invoker
class RemoteControl:
    def __init__(self):
        self._command = None
    def set_command(self, command):
        self._command = command
    def press_button(self):
        self._command.execute()
light = Light()
light_on_command = LightOnCommand(light)
light_off_command = LightOffCommand(light)
remote_control = RemoteControl()
remote_control.set_command(light_on_command)
remote_control.press_button()
remote_control.set_command(light_off_command)
remote_control.press_button()