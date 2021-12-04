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


def import_input(example=False):
    day = os.path.basename(sys.argv[0]).split('.')[0]
    if example:
        return open("input/example_input_" + day + ".txt")
    else:
        return open("input/input_" + day + ".txt")


def replace_chr(i, char, string):
    return string[:i] + char + string[i + 1:]


def replace_chrs(span, char, string):
    return string[:span[0]] + char + string[span[1]:]


def print_2d_array(array, el_length):
    for row in array:
        for el in row:
            if not el:
                print(' '*(el_length-1) + 'X', end=' ')
            else:
                print(str(el).zfill(el_length), end=' ')
        print()

