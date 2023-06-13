"""Simple, jcolorized messaging"""
import jmessaging.exceptions as exc
from jmessaging.jcolor import jcolor, jcolorize, jstyle
from jmessaging.jprint import print_same_line


class Message:
    """
    Class for messages
    """

    _left = "["
    _right = "]"

    def __init__(
        self, color: str = "default", style: str = "bold", background: str = "black"
    ) -> None:
        try:
            self._color = getattr(jcolor, color)
        except AttributeError as e:
            raise exc.InvalidColor(e)

        try:
            self._style = getattr(jstyle, style)
        except AttributeError as e:
            raise exc.InvalidStyle(e)

        try:
            self._background = getattr(jcolor, background)
        except AttributeError as e:
            raise exc.InvalidBackground(e)

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, new_color: str) -> None:
        self._color = new_color

    @property
    def background(self) -> str:
        return self._background

    @background.setter
    def background(self, new_background: str) -> None:
        self._background = new_background

    @property
    def style(self) -> str:
        return self._style

    @style.setter
    def style(self, new_style: str) -> None:
        self._style = new_style

    def __brackets(self, text: str):
        """
        Applies opening and closing brackets to the message level color (i.e.,
        `info`, `warning`, `error`)

        Args:
            level (dict): dict containing the message level color (i.e., `info`,
            `warning`, `error`) and the text (message) that gives the level of
            the message

        Returns:
            str: the message level string with the surrounding brackets and text
            color applied
        """
        left = jcolorize(self._left, self.color)
        right = jcolorize(f"{self._right}:", self.color)
        colorized_text = jcolorize(text)
        return "".join([left, colorized_text, right])

    def __call__(self, text: str) -> str:
        brackets = self.__brackets(text)
        colorized_text = f"{brackets} {jcolorize(text, self.color)}"
        return colorized_text

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        color = jcolor.name_map[self.color]
        style = jstyle.name_map[self.style]
        background = jcolor.name_map[self.background]
        string = f"<Message color: {color}, style: {style}, bg: {background}>"
        return string


class Messenger:
    """
    Class for printing messages to the console
    """

    _info = jcolor.white + jstyle.bold
    _warning = jcolor.yellow + jstyle.bold
    _error = jcolor.red + jstyle.bold

    _left = "["
    _right = "]"

    def __init__(self, color=jcolor.default):
        """
        Initializes the Messenger object.

        Args:
            color (jcolor, optional): The color of the text. Defaults to
            jcolor.default (white).
        """
        self.color = color

    def info(self, message, same_line=False):
        """
        Prints an informational message to the console

        Args:
            message (str): The message to be printed to the console
            same_line (bool, optional): Prints the message to the current after
            resetting that line. Defaults to False.
        """
        level = {"color": self._info, "text": "info"}
        self.__print(message, level, same_line)

    def warning(self, message, same_line=False):
        """
        Prints an warning message to the console

        Args:
            message (str): The message to be printed to the console
            same_line (bool, optional): Prints the message to the current after
            resetting that line. Defaults to False.
        """
        level = {"color": self._warning, "text": "warning"}
        self.__print(message, level, same_line)

    def error(self, message, same_line=False):
        """
        Prints an error message to the console

        Args:
            message (str): The message to be printed to the console
            same_line (bool, optional): Prints the message to the current after
            resetting that line. Defaults to False.
        """
        level = {"color": self._error, "text": "error"}
        self.__print(message, level, same_line)

    def __brackets(self, level):
        """
        Applies opening and closing brackets to the message level color (i.e.,
        `info`, `warning`, `error`)

        Args:
            level (dict): dict containing the message level color (i.e., `info`,
            `warning`, `error`) and the text (message) that gives the level of
            the message

        Returns:
            str: the message level string with the surrounding brackets and text
            color applied
        """
        left = jcolorize(self._left, self.color)
        right = jcolorize(f"{self._right}:", self.color)
        level_text = jcolorize(level["text"], level["color"])
        return "".join([left, level_text, right])

    def __print(self, message, level, same_line):
        """
        Prints the message to the console

        Args:
            message (str): The message text
            level (dict): A dict giving the message level and the corresponding
            color of the message
            same_line (bool): Should the message be printed to a new line
            (False) or to the same line (True)
        """
        brackets = self.__brackets(level)
        text = f"{brackets} {jcolorize(message, self.color)}"
        if not same_line:
            print(text)
        else:
            print_same_line(text)
