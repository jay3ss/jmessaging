"""Simple, jcolorized messaging"""
from jmessaging.jcolor import jcolor, jcolorize, jstyle


class Messenger:
    _info = jcolor.white + jstyle.bold
    _warning = jcolor.yellow + jstyle.bold
    _error = jcolor.red + jstyle.bold

    _left = "["
    _right = "]"

    def __init__(self, color=jcolor.default):
        self.color = color

    def info(self, message, same_line=False):
        level = {"color": self._info, "text": "info"}
        self.__print(message, level, same_line)

    def warning(self, message, same_line=False):
        level = {"color": self._warning, "text": "warning"}
        self.__print(message, level, same_line)

    def error(self, message, same_line=False):
        level = {"color": self._error, "text": "error"}
        self.__print(message, level, same_line)

    def __brackets(self, level):
        left = jcolorize(self._left, self.color)
        right = jcolorize(f"{self._right}:", self.color)
        level_text = jcolorize(level["text"], level["color"])
        return ''.join([left, level_text, right])

    def __print(self, message, level, same_line):
        brackets = self.__brackets(level)
        text = f"{brackets} {jcolorize(message, self.color)}"
        if not same_line:
            print(text)
        else:
            print('\r', text, end='', flush=True, sep='')
