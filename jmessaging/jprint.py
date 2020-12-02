"""Printing-related"""


def print_same_line(*msg):
    """Prints on the same line in the terminal

    Args:
        msg: The message to be printed

    Got some help from https://stackoverflow.com/a/5419488/3562890
    """
    clear = '\x1b[1K\r'
    print(clear, *msg, end='', flush=True, sep='')
