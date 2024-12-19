# Day 19 of Advent of Code 2024
# Linen Layout

import unittest
from functools import cache

from aoc.helpers import import_input, parse_input


def parser(inputs):
    towels, designs = inputs.split("\n\n")
    towels = set(towels.split(", "))
    designs = designs.split("\n")
    return towels, designs


@parse_input(parser)
def part1(inputs):
    @cache
    def find_paths(design, start):
        if start == len(design):
            return True
        for towel in towels:
            end = start + len(towel)
            if design[start:end] == towel and find_paths(design, end):
                return True
        return False

    towels, designs = inputs
    return sum(find_paths(design, 0) for design in designs)


@parse_input(parser)
def part2(inputs):
    @cache
    def find_paths(design, start):
        if start == len(design):
            return 1
        paths = 0
        for towel in towels:
            end = start + len(towel)
            if design[start:end] == towel:
                paths += find_paths(design, end)
        return paths

    towels, designs = inputs
    return sum(find_paths(design, 0) for design in designs)


class Tests202419(unittest.TestCase):
    inputs = "r, wr, b, g, bwu, rb, gb, br\n\nbrwrr\nbggr\ngbbr\nrrbgbr\nubwu\nbwurrg\nbrgr\nbbrgwb"

    def test_part1(self):
        expected = 6
        self.assertEqual(expected, part1(self.inputs))

    def test_part2(self):
        expected = 16
        self.assertEqual(expected, part2(self.inputs))


if __name__ == "__main__":
    inputs = import_input()
    print("part 1:", part1(inputs))
    print("part 2:", part2(inputs))
