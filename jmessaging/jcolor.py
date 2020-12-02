"""Print colors to the terminal! Much inspiration taken from
https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python
"""
import os


os.system("")


class jcolor:
    black = '\33[30m'
    red = '\33[31m'
    green = '\33[32m'
    yellow = '\33[33m'
    blue = '\33[34m'
    magenta = '\33[35m'
    cyan = '\33[36m'
    white = '\33[37m'
    default = '\33[39m'
    gray = '\33[90m'

    bright_red = '\33[91m'
    bright_green = '\33[92m'
    bright_yellow = '\33[93m'
    bright_blue = '\33[94m'
    bright_magenta = '\33[95m'
    bright_cyan = '\33[96m'
    bright_white = '\33[97m'

    def __add__(cls, other):
        return cls.value + other.value


class jstyle:
    reset = '\33[0m'
    bold = '\33[1m'
    italics = '\33[3m'
    underline = '\33[4m'
    blink = '\33[5m'
    selected = '\33[7m'
    strike = '\33[8m'

    def __add__(cls, other):
        return cls.value + other.value


class jbackground:
    black = '\33[40m'
    red = '\33[41m'
    green = '\33[42m'
    yellow = '\33[43m'
    blue = '\33[44m'
    magenta = '\33[45m'
    cyan = '\33[46m'
    white = '\33[47m'
    gray = '\33[100m'

    bright_red = '\33[101m'
    bright_green = '\33[102m'
    bright_yellow = '\33[103m'
    bright_blue = '\33[104m'
    bright_magenta = '\33[105m'
    bright_cyan = '\33[106m'
    bright_white = '\33[107m'

    def __add__(cls, other):
        return cls.value + other.value


def jcolorize(msg, *args):
    reset = jstyle.reset
    styles = ''.join(args)
    return styles + msg + reset
