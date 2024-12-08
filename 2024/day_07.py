# Day 07 of Advent of Code 2024
# Bridge Repair

import math
import unittest

from aoc.helpers import import_input, parse_input


def parser(inputs):
    equations = []
    for line in inputs.split("\n"):
        test, numbers = line.split(": ")
        equations.append((int(test), list(map(int, numbers.split()))))
    return equations


def solve(test, numbers, with_concat=False):
    paths = [(numbers[0], 1)]
    while len(paths) > 0:
        total, i = paths.pop()
        if i == len(numbers):
            if total == test:
                return test
            continue
        number = numbers[i]
        if with_concat:
            # https://math.stackexchange.com/questions/578069/is-there-an-algebraic-method-to-concat-two-numbers
            concatenated_number = total * math.pow(10, (1 + math.floor(math.log10(number)))) + number
            paths.append((concatenated_number, i + 1))
        paths.append((total * number, i + 1))
        paths.append((total + number, i + 1))
    return 0


@parse_input(parser)
def part1(equations):
    total = 0
    for test, numbers in equations:
        total += solve(test, numbers)
    return total


@parse_input(parser)
def part2(equations):
    total = 0
    for test, numbers in equations:
        total += solve(test, numbers, True)
    return total


class Tests202407(unittest.TestCase):
    inputs = (
        "190: 10 19\n"
        "3267: 81 40 27\n"
        "83: 17 5\n"
        "156: 15 6\n"
        "7290: 6 8 6 15\n"
        "161011: 16 10 13\n"
        "192: 17 8 14\n"
        "21037: 9 7 18 13\n"
        "292: 11 6 16 20"
    )

    def test_part1(self):
        expected = 3749
        self.assertEqual(expected, part1(self.inputs))

    def test_part2(self):
        expected = 11387
        self.assertEqual(expected, part2(self.inputs))


if __name__ == "__main__":
    inputs = import_input()
    print("part 1:", part1(inputs))
    print("part 2:", part2(inputs))
