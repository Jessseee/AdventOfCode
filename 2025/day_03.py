# Day 03 of Advent of Code 2025
# Lobby

import unittest

from aoc.helpers import import_input, timer


def parser(inputs):
    return [list(map(int, line)) for line in inputs.split("\n")]


@timer()
def part1(inputs):
    total = 0
    for bank in inputs:
        i = bank.index(max(bank[:-1]))
        j = bank.index(max(bank[i+1:]))
        total += bank[i] * 10 + bank[j]
    return total


@timer()
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
    inputs = "98765432111111\n811111111111119\n234234234234278\n818181911112111"

    def test_part1(self):
        expected = 357
        self.assertEqual(expected, part1(self.inputs))

    def test_part2(self):

        expected = 3121910778619
        self.assertEqual(expected, part2(self.inputs))


if __name__ == "__main__":
    inputs = import_input(parser=parser)
    part1(inputs)
    part2(inputs)
