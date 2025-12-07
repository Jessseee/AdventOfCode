# Day 04 of Advent of Code 2025
# Printing Department

import unittest
from copy import deepcopy

import numpy as np

from aoc.helpers import import_input, parse_input
from aoc.library.grid import get_neighbours_within_bound, cardinal_directions


def parser(inputs):
    return np.array(list(map(list, inputs.split("\n"))))


@parse_input(parser)
def part1(inputs: np.ndarray):
    accessible = 0
    max_x, max_y = inputs.shape
    rolls = [pos for pos, value in np.ndenumerate(inputs) if value == "@"]
    for (x, y) in rolls:
        neighbours = get_neighbours_within_bound(x, y, directions=cardinal_directions(), max_x=max_x, max_y=max_y)
        if sum(inputs[nx, ny] == "@" for (nx, ny) in neighbours) < 4:
            accessible += 1
    return accessible


@parse_input(parser)
def part2(inputs):
    removed = 0
    to_remove = set()
    max_x, max_y = inputs.shape
    rolls = {
        (x, y): get_neighbours_within_bound(x, y, directions=cardinal_directions(), max_x=max_x, max_y=max_y)
        for (x, y), value in np.ndenumerate(inputs) if value == "@"
    }
    while True:
        for (x, y), neighbours in rolls.items():
            if sum((nx, ny) in rolls for (nx, ny) in neighbours) < 4:
                to_remove.add((x, y))
        if len(to_remove) == 0:
            break
        for (x, y) in to_remove:
            del rolls[(x, y)]
        removed += len(to_remove)
        to_remove.clear()
    return removed


class Tests202504(unittest.TestCase):
    inputs = (
        "..@@.@@@@.\n"
        "@@@.@.@.@@\n"
        "@@@@@.@.@@\n"
        "@.@@@@..@.\n"
        "@@.@@@@.@@\n"
        ".@@@@@@@.@\n"
        ".@.@.@.@@@\n"
        "@.@@@.@@@@\n"
        ".@@@@@@@@.\n"
        "@.@.@@@.@."
    )

    def test_part1(self):
        expected = 13
        self.assertEqual(expected, part1(self.inputs))

    def test_part2(self):
        expected = 43
        self.assertEqual(expected, part2(self.inputs))


if __name__ == "__main__":
    inputs = import_input()
    print("part 1:", part1(inputs))
    print("part 2:", part2(inputs))
