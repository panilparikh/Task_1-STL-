class TextComponent:
    def get_text(self):
        pass
class PlainText(TextComponent):
    def __init__(self, content):
        self._content = content
    def get_text(self):
        return self._content
class TextDecorator(TextComponent):
    def __init__(self, text_component):
        self._text_component = text_component
    def get_text(self):
        return self._text_component.get_text()
class BoldDecorator(TextDecorator):
    def get_text(self):
        return f"<b>{super().get_text()}</b>"
class ItalicDecorator(TextDecorator):
    def get_text(self):
        return f"<i>{super().get_text()}</i>"