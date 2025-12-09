import os
import re
import sys
import timeit
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
    if split is not None and parser is not None:
        inputs = list(map(parser, inputs))
    elif parser:
        inputs = parser(inputs)
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


def format_timeit(t):
    """Format a time duration (in seconds, float) to a human-friendly string"""
    if t < 1e-6:
        return f"{t * 1e9:.3f}ns"
    if t < 1e-3:
        return f"{t * 1e6:.3f}µs"
    if t < 1:
        return f"{t * 1000:.3f}ms"
    if t < 60:
        return f"{t:.3f}s"
    return f"{int(t // 60)}:{t % 60:06.3f}"


def timer(show_result=True):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = timeit.default_timer()
            result = func(*args, **kwargs)
            end = timeit.default_timer()
            if show_result:
                print(f"[{format_timeit(end - start)}]\t{func.__name__}: {result}")
            else:
                print(f"[{format_timeit(end - start)}]\t{func.__name__}")
            return result
        return wrapper
    return decorator


def integers_from_string(string):
    return list(map(int, re.findall(r"-?\d+", string)))
