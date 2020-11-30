"""Print colors to the terminal! Much inspiration taken from
https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python
"""
import os


os.system("")


class Color:
    BLACK = '\33[30m'
    RED = '\33[31m'
    GREEN = '\33[32m'
    YELLOW = '\33[33m'
    BLUE = '\33[34m'
    VIOLET = '\33[35m'
    BEIGE = '\33[36m'
    WHITE2 = '\33[37m'

    GREY = '\33[90m'
    RED2 = '\33[91m'
    GREEN2 = '\33[92m'
    YELLOW2 = '\33[93m'
    BLUE2 = '\33[94m'
    VIOLET2 = '\33[95m'
    BEIGE2 = '\33[96m'
    WHITE = '\33[97m'

    def __add__(cls, other):
        return cls.value + other.value


class Style:
    RESET = '\33[0m'
    BOLD = '\33[1m'
    ITALICS = '\33[3m'
    UNDERLINE = '\33[4m'
    BLINK = '\33[5m'
    BLINK2 = '\33[6m'
    SELECTED = '\33[7m'
    STRIKE = '\33[8m'

    def __add__(cls, other):
        return cls.value + other.value


class Background:
    BLACK = '\33[40m'
    RED = '\33[41m'
    GREEN = '\33[42m'
    YELLOW = '\33[43m'
    BLUE = '\33[44m'
    VIOLET = '\33[45m'
    BEIGE = '\33[46m'
    WHITE = '\33[47m'

    GREY = '\33[100m'
    RED2 = '\33[101m'
    GREEN2 = '\33[102m'
    YELLOW2 = '\33[103m'
    BLUE2 = '\33[104m'
    VIOLET2 = '\33[105m'
    BEIGE2 = '\33[106m'
    WHITE2 = '\33[107m'

    def __add__(cls, other):
        return cls.value + other.value


def colorize(msg, *args):
    reset = Style.RESET
    styles = ''.join(args)
    return styles + msg + reset
