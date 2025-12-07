# Day 06 of Advent of Code 2025
# Trash Compactor

import re
import unittest
from itertools import groupby
from math import prod

from aoc.helpers import import_input, parse_input

OPERATOR = {"+": sum, "*": prod}


def parser(inputs):
    lines = inputs.split("\n")
    return lines[:-1], lines[-1]


@parse_input(parser)
def part1(inputs):
    numbers, operators = inputs
    problems = list(zip(*[map(int, re.findall(r"\d+", line)) for line in numbers]))
    operators = [OPERATOR[operator] for operator in operators.split()]
    return sum(operator(numbers) for numbers, operator in zip(problems, operators))


@parse_input(parser)
def part2(inputs):
    numbers, operators = inputs
    problems_rearranged = map(str.strip, map(''.join, zip(*numbers)))
    problems_grouped = groupby(problems_rearranged , lambda x: x == '')
    problems = [list(map(int, group)) for is_delim, group in problems_grouped if not is_delim]
    operators = [OPERATOR[operator] for operator in operators.split()]
    return sum(operator(numbers) for numbers, operator in zip(problems, operators))


class Tests202506(unittest.TestCase):
    inputs = "123 328  51 64 \n 45 64  387 23 \n  6 98  215 314\n*   +   *   +  "

    def test_part1(self):
        expected = 4277556
        self.assertEqual(expected, part1(self.inputs))

    def test_part2(self):
        expected = 3263827
        self.assertEqual(expected, part2(self.inputs))


if __name__ == "__main__":
    inputs = import_input()
    print("part 1:", part1(inputs))
    print("part 2:", part2(inputs))
