# Some small functions to use in the different solutions
import sys
import os
import re


def color_text(text, color_code):
    """
    :param Any text: The text to be colored
    :param int color_code: The ANSI color code
    :return: ANSI escape sequence
    Color text for display in console using ANSI escape sequence
    """
    return f'\033[{color_code}m{str(text)}\033[0m'


def import_input(split=None, type=None, **kwargs):
    """
    :param bool example: Should import example input instead
    :param str split: string to split input on
    :param Type type: type to cast input
    :return: inputs from input file
    Import input for day of puzzle
    """
    day = re.findall('[0-9]+', os.path.basename(sys.argv[0]))[0]
    path = "input/example_input_day_" + day + ".txt" if kwargs.get('example') else "input/input_day_" + day + ".txt"
    inputs = open(path)
    if split is not None:
        inputs = inputs.read().split(split)
    if type is not None:
        inputs = list(map(type, inputs))
    return inputs


def replace_chr(i, char, string):
    """
    :param int i: Index of character to replace
    :param str char: Character(s) to place in string
    :param str string: String to replace character in
    :return: String with character replaced
    Replace a character in a string
    """
    return string[:i] + char + string[i + 1:]


def replace_chrs(span, char, string):
    """
    :param list span: Start and end of span to replace
    :param str char: Character(s) to place in string
    :param str string: String to replace characters in
    :return: String with characters replaced
    Replace a span of characters in a string
    """
    return string[:span[0]] + char + string[span[1]:]


def print_2d_array(array, el_length=1):
    """
    :param list[list]|ndarray array: 2d array to print
    :param int el_length: the length of each element in the array
    Nicely print a 2d array
    """
    for row in array:
        for el in row:
            if not el:
                print(' '*(el_length-1) + '.', end=' ')
            else:
                print(str(el).zfill(el_length), end=' ')
        print()
