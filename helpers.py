# Some small functions to use in the different solutions
import sys
import os


def color_text(text, color_code):
    """
    :param Any text: The text to be colored
    :param int color_code: The ANSI color code
    :return: ANSI escape sequence
    Color text for display in console using ANSI escape sequence
    """
    return f'\033[{color_code}m{text}\033[0m'


def import_input():
    day = os.path.basename(sys.argv[0]).split('.')[0]
    return open("input/input_" + day + ".txt")