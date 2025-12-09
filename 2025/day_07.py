# Day 07 of Advent of Code 2025
# Laboratories

import unittest
from collections import deque
from functools import cache

import numpy as np

from aoc.helpers import import_input, timer


def parser(inputs):
    grid = np.array([list(line) for line in inputs.split("\n")])
    start = tuple([int(i[0]) for i in np.where(grid == "S")])
    return grid, start


@timer()
def part1(inputs):
    grid, start = inputs

    to_visit = deque([start])
    explored = {start}
    splitters = 0
    while len(to_visit):
        (row, col) = to_visit.pop()
        explored.add((row, col))

        row += 1
        if (row, col) in explored or row >= len(grid):
            continue
        if grid[(row, col)] == "^":
            splitters += 1
            for split in [(row, col + 1), (row, col - 1)]:
                to_visit.appendleft(split)
            continue
        to_visit.append((row, col))

    return splitters


@timer()
def part2(inputs):
    grid, start = inputs

    @cache
    def follow_beam(row, col, paths=0):
        row += 1
        if row >= len(grid):
            return paths + 1
        if grid[row, col] == "^":
            return follow_beam(row, col + 1, paths) + follow_beam(row, col - 1, paths)
        return follow_beam(row, col, paths)

    return follow_beam(*start)


class Tests202507(unittest.TestCase):
    inputs = (
        ".......S.......\n"
        "...............\n"
        ".......^.......\n"
        "...............\n"
        "......^.^......\n"
        "...............\n"
        ".....^.^.^.....\n"
        "...............\n"
        "....^.^...^....\n"
        "...............\n"
        "...^.^...^.^...\n"
        "...............\n"
        "..^...^.....^..\n"
        "...............\n"
        ".^.^.^.^.^...^.\n"
        "..............."
    )

    def test_part1(self):
        expected = 21
        self.assertEqual(expected, part1(self.inputs))

    def test_part2(self):
        expected = 40
        self.assertEqual(expected, part2(self.inputs))


if __name__ == "__main__":
    inputs = import_input(parser=parser)
    part1(inputs)
    part2(inputs)
