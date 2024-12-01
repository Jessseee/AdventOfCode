# Day 01 of Advent of Code 2024
# Historian Hysteria

import unittest
from collections import Counter

from aoc.helpers import import_input, parse_input


def parser(inputs):
    return list(zip(*[line.split("   ") for line in inputs.split("\n")]))


@parse_input(parser)
def part1(inputs):
    left_list, right_list = inputs
    return sum(map(lambda x: abs(int(x[0]) - int(x[1])), zip(sorted(left_list), sorted(right_list))))


@parse_input(parser)
def part2(inputs):
    left_list, right_list = inputs
    counter = Counter(right_list)
    return sum(int(num) * counter[num] for num in left_list)


class Tests202401(unittest.TestCase):
    inputs = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"

    def test_part1(self):
        expected = 11
        self.assertEqual(expected, part1(self.inputs))

    def test_part2(self):
        expected = 31
        self.assertEqual(expected, part2(self.inputs))


if __name__ == "__main__":
    inputs = import_input()
    print("part 1:", part1(inputs))
    print("part 2:", part2(inputs))
