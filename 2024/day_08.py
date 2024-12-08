# Day 08 of Advent of Code 2024
# Resonant Collinearity

import unittest
from collections import defaultdict
from itertools import product

from aoc.helpers import import_input, parse_input


def parser(grid):
    grid = [list(row) for row in grid.split("\n")]
    rows = len(grid)
    cols = len(grid[0])
    frequencies = defaultdict(list)
    for y in range(rows):
        for x in range(cols):
            cell = grid[y][x]
            if cell != ".":
                frequencies[cell].append((x, y))
    return frequencies, lambda x, y: 0 <= x < cols and 0 <= y < cols


@parse_input(parser)
def part1(inputs):
    frequencies, in_bound = inputs
    antinodes = set()
    for frequency, antennas in frequencies.items():
        for (x1, y1), (x2, y2) in product(antennas, repeat=2):
            if (x1, y1) == (x2, y2):
                continue
            nx, ny = x2 + (x2 - x1), y2 + (y2 - y1)
            if in_bound(nx, ny):
                antinodes.add((nx, ny))
    return len(antinodes)


@parse_input(parser)
def part2(inputs):
    frequencies, in_bound = inputs
    antinodes = set()
    for frequency, antennas in frequencies.items():
        for (x1, y1), (x2, y2) in product(antennas, repeat=2):
            if (x1, y1) == (x2, y2):
                continue
            dx, dy = (x2 - x1), (y2 - y1)
            nx, ny = x1, y1
            while in_bound(nx := nx + dx, ny := ny + dy):
                antinodes.add((nx, ny))
    return len(antinodes)


class Tests202408(unittest.TestCase):
    inputs = (
        "............\n"
        "........0...\n"
        ".....0......\n"
        ".......0....\n"
        "....0.......\n"
        "......A.....\n"
        "............\n"
        "............\n"
        "........A...\n"
        ".........A..\n"
        "............\n"
        "............"
    )

    def test_part1(self):
        expected = 14
        self.assertEqual(expected, part1(self.inputs))

    def test_part2(self):
        expected = 34
        self.assertEqual(expected, part2(self.inputs))


if __name__ == "__main__":
    inputs = import_input()
    print("part 1:", part1(inputs))
    print("part 2:", part2(inputs))
