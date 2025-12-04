# Day 03 of Advent of Code 2025
# Lobby

import unittest

from aoc.helpers import import_input, parse_input


def parser(inputs):
    return [list(map(int, line)) for line in inputs.split("\n")]


@parse_input(parser)
def part1(inputs):
    total = 0
    for bank in inputs:
        i = bank.index(max(bank[:-1]))
        j = bank.index(max(bank[i+1:]))
        total += bank[i] * 10 + bank[j]
    return total


@parse_input(parser)
def part2(inputs):
    total = 0
    for bank in inputs:
        bank = list(enumerate(bank))
        value, j = 0, 0
        for i in range(11, -1, -1):
            j, n = max(bank[j:len(bank)-i], key=lambda x: x[1])
            value += n * 10 ** i
            j += 1
        total += value
    return total


class Tests202503(unittest.TestCase):
    def test_part1(self):
        inputs = "98765432111111\n811111111111119\n234234234234278\n818181911112111"
        expected = 357
        self.assertEqual(expected, part1(inputs))

    def test_part2(self):
        inputs = "98765432111111\n811111111111119\n234234234234278\n818181911112111"
        expected = 3121910778619
        self.assertEqual(expected, part2(inputs))


if __name__ == "__main__":
    inputs = import_input()
    print("part 1:", part1(inputs))
    print("part 2:", part2(inputs))
