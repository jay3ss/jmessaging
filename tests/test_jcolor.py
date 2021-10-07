"""
Test module for the jcolor module
"""
import jmessaging as jm


def test_colors():
    """
    Test that colors have been correctly applied
    """
    reset = '\33[0m'
    msg = 'Testing colors, this should be green'
    green = '\33[32m'
    text = green + msg + reset
    assert(text == jm.jcolorize(msg, jm.jcolor.green))


def test_styles():
    """
    Test that styles have been correctly applied
    """
    reset = '\33[0m'
    msg = 'Testing styles, this should be italicized'
    italics = '\33[3m'
    text = italics + msg + reset
    assert(text == jm.jcolorize(msg, jm.jstyle.italics))


def test_backgrounds():
    """
    Test that backgrounds have been correctly applied
    """
    reset = '\33[0m'
    msg = 'Testing backgrounds, this should have a red background'
    red_bg = '\33[41m'
    text = red_bg + msg + reset
    assert(text == jm.jcolorize(msg, jm.jbackground.red))
