"""
Test module for the jmessaging module
"""
import pytest

import jmessaging as jm
import jmessaging.exceptions as exc


def setup_level_text(level):
    bold = "\33[1m"
    level_color = dict(info="\33[37m", warning="\33[33m", error="\33[31m")
    reset = "\33[0m"
    text_color = f"{level_color[level]}{bold}"
    bracket_color = f"\33[39m"

    left = f"{bracket_color}[{reset}"
    right = f"{bracket_color}]:{reset}"
    level_text = f"{text_color}{level}{reset}"

    return f"{left}{level_text}{right}"


def test_info_brackets(messenger):
    """
    Test that the brackets on an info message have been correctly applied
    """
    text = setup_level_text("info")
    level = {"text": "info", "color": messenger._info}
    msg = messenger._Messenger__brackets(level)
    assert msg == text


def test_warning_brackets(messenger):
    """
    Test that the brackets on an warning message have been correctly applied
    """
    text = setup_level_text("warning")
    level = {"text": "warning", "color": messenger._warning}
    msg = messenger._Messenger__brackets(level)
    assert msg == text


def test_error_brackets(messenger):
    """
    Test that the brackets on an error message have been correctly applied
    """
    text = setup_level_text("error")
    level = {"text": "error", "color": messenger._error}
    msg = messenger._Messenger__brackets(level)
    assert msg == text


def test_message_defaults(message):
    """
    Test that the defaults in the message work
    """
    text = "test message"
    assert text in message(text)


def test_incorrect_background_raises_exception():
    with pytest.raises(exc.InvalidBackground):
        jm.Message(background="this color doesn't exist")


def test_incorrect_color_raises_exception():
    with pytest.raises(exc.InvalidColor):
        jm.Message(color="this color doesn't exist")


def test_incorrect_style_raises_exception():
    with pytest.raises(exc.InvalidStyle):
        jm.Message(style="this style doesn't exist")
