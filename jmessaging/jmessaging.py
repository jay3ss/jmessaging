"""Simple, colorized messaging"""
from jcolor import colorize
from jcolor import Color, Style


class Messenger:
    INFO = Color.WHITE + Style.BOLD
    WARNING = Color.YELLOW + Style.BOLD
    ERROR = Color.RED + Style.BOLD

    LEFT = "["
    RIGHT = "]"

    def __init__(self, color=Color.WHITE):
        self.color = color

    def info(self, message, same_line=False):
        level = {"color": self.INFO, "text": "INFO"}
        self.__print(message, level, same_line)

    def warning(self, message, same_line=False):
        level = {"color": self.WARNING, "text": "WARNING"}
        self.__print(message, level, same_line)

    def error(self, message, same_line=False):
        level = {"color": self.ERROR, "text": "ERROR"}
        self.__print(message, level, same_line)

    def __brackets(self, level):
        left = colorize(self.LEFT, self.color)
        right = colorize(f"{self.RIGHT}:", self.color)
        level_text = colorize(level["text"], level["color"])
        return ''.join([left, level_text, right])

    def __print(self, message, level, same_line):
        brackets = self.__brackets(level)
        text = f"{brackets} {colorize(message, self.color)}"
        if not same_line:
            print(text)
        else:
            print('\r', text, end='', flush=True, sep='')
