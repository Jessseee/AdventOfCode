# Some utility function for importing and parsing data.
import sys
import os
import re

from typing import Callable, Any
from typing.io import IO


def import_input(split: str = None, parser: Callable[[str], Any] = None, example: bool = False) -> list|IO:
    """
    Import input or example data from text file.

    :param split: string to split input on.
    :param parser: function to further parse data.
    :param example: Should import example input instead.
    :return: inputs from input file.
    """
    day = re.findall('[0-9]+', os.path.basename(sys.argv[0]))[0]
    path = "input/example_input_day_" + day + ".txt" if example else "input/input_day_" + day + ".txt"
    if not os.path.isfile(path): raise FileNotFoundError(f"Input file does not exist at {path}")
    inputs = open(path)
    if split is not None:
        if split == '': inputs = [char for char in inputs.read()]
        else: inputs = inputs.read().split(split)
    if parser is not None:
        inputs = list(map(parser, inputs))
    return inputs


def replace_chr(i, char, string):
    """
    Replace a character in a string.

    :param int i: Index of character to replace.
    :param str char: Character(s) to place in string.
    :param str string: String to replace character in.
    :return: String with character replaced.
    """
    return string[:i] + char + string[i + 1:]


def replace_chrs(span, char, string):
    """
    Replace a span of characters in a string.

    :param list span: Start and end of span to replace.
    :param str char: Character(s) to place in string.
    :param str string: String to replace characters in.
    :return: String with characters replaced.
    """
    return string[:span[0]] + char + string[span[1]:]



