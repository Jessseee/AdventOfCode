import os
import re
import sys
from inspect import signature
from typing import Any, Callable, Optional
from functools import wraps


def import_input(
        split: Optional[str] = None,
        parser: Optional[Callable[[str], Any]] = None,
        example: bool = False
):
    """
    Import input or example data from text file.

    :param split: string to split input on.
    :param parser: function to further parse data.
    :param example: Should import example input instead.
    :return: inputs from input file.
    """
    day = re.findall("[0-9]+", os.path.basename(sys.argv[0]))[0]
    filename = "example_input_day_" + day + ".txt" if example else "input_day_" + day + ".txt"
    path = os.path.join(os.path.dirname(sys.argv[0]), "input", filename)
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Input file does not exist at {path}")
    inputs = open(path).read()
    if split is not None:
        if split == "":
            inputs = [char for char in inputs]
        else:
            inputs = inputs.split(split)
    if parser is not None:
        inputs = list(map(parser, inputs))
    return inputs


def parse_input(parser: Callable[[str], Any]):
    """
    Decorator to parse first argument of a function or an argument named 'inputs'.

    :param parser: The function to parse the inputs with.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            mapping = signature(func).bind(*args, **kwargs)
            input_var = mapping.arguments.get("inputs")
            if input_var is not None:
                mapping.arguments["inputs"] = parser(input_var)
            else:
                first_argument = list(mapping.arguments.keys())[0]
                input_var = mapping.arguments.get(first_argument)
                mapping.arguments[first_argument] = parser(input_var)
            return func(*mapping.args, **mapping.kwargs)
        return wrapper
    return decorator


def replace_chr(i: int, char: str, string: str) -> str:
    """
    Replace a character in a string.

    :param int i: Index of character to replace.
    :param str char: Character(s) to place in string.
    :param str string: String to replace character in.
    :return: String with character replaced.
    """
    return string[:i] + char + string[i + 1 :]


def replace_chrs(span: list[int, int], char: str, string: str) -> str:
    """
    Replace a span of characters in a string.

    :param span: Start and end of span to replace.
    :param char: Character(s) to place in string.
    :param string: String to replace characters in.
    :return: String with characters replaced.
    """
    return string[: span[0]] + char + string[span[1] :]


def parse_integers(string: str) -> list[int]:
    """
    Parse all integers in a string.

    :param string: The string to parse.
    :return: A list of the parsed integers.
    """
    return list(map(int, re.findall(r"[+-]?\d+", string)))
