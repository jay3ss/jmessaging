"""Print colors to the terminal! Much inspiration taken from
https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python
"""
import os


os.system("")


class jcolor:
    """
    Provides font colors for the text to be printed to the console
    """

    black = "\33[30m"
    red = "\33[31m"
    green = "\33[32m"
    yellow = "\33[33m"
    blue = "\33[34m"
    magenta = "\33[35m"
    cyan = "\33[36m"
    white = "\33[37m"
    default = "\33[39m"
    gray = "\33[90m"

    bright_red = "\33[91m"
    bright_green = "\33[92m"
    bright_yellow = "\33[93m"
    bright_blue = "\33[94m"
    bright_magenta = "\33[95m"
    bright_cyan = "\33[96m"
    bright_white = "\33[97m"

    name_map = {
        "\33[30m": "black",
        "\33[31m": "red",
        "\33[32m": "green",
        "\33[33m": "yellow",
        "\33[34m": "blue",
        "\33[35m": "magenta",
        "\33[36m": "cyan",
        "\33[37m": "white",
        "\33[39m": "default",
        "\33[90m": "gray",
        "\33[91m": "bright_red",
        "\33[92m": "bright_green",
        "\33[93m": "bright_yellow",
        "\33[94m": "bright_blue",
        "\33[95m": "bright_magenta",
        "\33[96m": "bright_cyan",
        "\33[97m": "bright_white",
    }

    def __add__(cls, other):
        return cls.value + other.value


class jstyle:
    """
    Provides styling for the text to be printed to the console
    """

    reset = "\33[0m"
    bold = "\33[1m"
    italics = "\33[3m"
    underline = "\33[4m"
    blink = "\33[5m"
    selected = "\33[7m"
    strike = "\33[8m"

    name_map = {
        "\33[0m": "reset",
        "\33[1m": "bold",
        "\33[3m": "italics",
        "\33[4m": "underline",
        "\33[5m": "blink",
        "\33[7m": "selected",
        "\33[8m": "strike",
    }

    def __add__(cls, other):
        return cls.value + other.value


class jbackground:
    """
    Provides background colors for the text to be printed to the console
    """

    black = "\33[40m"
    red = "\33[41m"
    green = "\33[42m"
    yellow = "\33[43m"
    blue = "\33[44m"
    magenta = "\33[45m"
    cyan = "\33[46m"
    white = "\33[47m"
    gray = "\33[100m"

    bright_red = "\33[101m"
    bright_green = "\33[102m"
    bright_yellow = "\33[103m"
    bright_blue = "\33[104m"
    bright_magenta = "\33[105m"
    bright_cyan = "\33[106m"
    bright_white = "\33[107m"

    name_map = {
        "\33[40m": "black",
        "\33[41m": "red",
        "\33[42m": "green",
        "\33[43m": "yellow",
        "\33[44m": "blue",
        "\33[45m": "magenta",
        "\33[46m": "cyan",
        "\33[47m": "white",
        "\33[100m": "gray",
        "\33[101m": "bright_red",
        "\33[102m": "bright_green",
        "\33[103m": "bright_yellow",
        "\33[104m": "bright_blue",
        "\33[105m": "bright_magenta",
        "\33[106m": "bright_cyan",
        "\33[107m": "bright_white",
    }

    def __add__(cls, other):
        return cls.value + other.value


def jcolorize(msg, *args):
    """
    [summary]

    Args:
        msg (str): the text to be colorized
        args (str): the styles (i.e., background, font colors, and styling)

    Returns:
        str: the text with any background, font colors, and styling applied
    """
    reset = jstyle.reset
    styles = "".join(args)
    return styles + msg + reset
