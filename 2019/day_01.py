# Day 01 of Advent of Code 2019
# The Tyranny of the Rocket Equation

import unittest

from aoc.helpers import *


def calculate_mass(mass) -> int:
    return mass // 3 - 2


def part1(masses: list[int]) -> int:
    return sum(map(calculate_mass, masses))


def part2(masses: list[int]) -> int:
    total = 0
    for mass in masses:
        while mass > 0:
            total += (mass := max(0, calculate_mass(mass)))
    return total


class Tests201901(unittest.TestCase):
    def test_part1(self):
        input = [12, 14, 1969, 100756]
        expected = 2 + 2 + 654 + 33583
        self.assertEqual(part1(input), expected)

    def test_part2(self):
        input = [14]
        expected = 2
        self.assertEqual(part2(input), expected)


if __name__ == "__main__":
    inputs = import_input("\n", int)
    print("part 1:", part1(inputs))
    print("part 2:", part2(inputs))
