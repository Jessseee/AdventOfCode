# Day 01 of Advent of Code 2025
# Secret Entrance

import unittest

from aoc.helpers import import_input, parse_input


def parse(inputs):
    return [(input[0], int(input[1:])) for input in inputs.split("\n")]


@parse_input(parse)
def part1(inputs):
    pos = 50
    password = 0
    for dir, n in inputs:
        pos = (pos + n if dir == "R" else pos - n) % 100
        password += pos == 0
    return password


@parse_input(parse)
def part2(inputs):
    pos = 50
    password = 0
    for dir, n in inputs:
        raw = (pos + n if dir == "R" else pos - n)
        password += (abs(raw) // 100) + (pos and raw <= 0)
        pos = raw % 100
    return password


class Tests202501(unittest.TestCase):
    inputs = "L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82"

    def test_part1(self):
        expected = 3
        self.assertEqual(expected, part1(self.inputs))

    def test_part2(self):
        expected = 6
        self.assertEqual(expected, part2(self.inputs))


if __name__ == "__main__":
    inputs = import_input()
    print("part 1:", part1(inputs))
    print("part 2:", part2(inputs))
