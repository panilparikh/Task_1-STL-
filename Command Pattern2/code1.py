class RemoteControl:
    def __init__(self):
        self._command = None
    def set_command(self, command):
        self._command = command
    def press_button(self):
        self._command.execute()