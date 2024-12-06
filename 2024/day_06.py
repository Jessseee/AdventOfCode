# Day 06 of Advent of Code 2024
# Guard Gallivant

import unittest

from aoc.helpers import import_input, parse_input


def parser(grid):
    return [list(row) for row in grid.split("\n")]


def find_guard(grid):
    rows = len(grid)
    cols = len(grid[0])
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == "^":
                return x, y


def step(position, direction):
    return position[0] + direction[0], position[1] + direction[1]


def find_loop(grid, obstacle, position, direction):
    rows = len(grid)
    cols = len(grid[0])
    visited = {(position, direction)}
    while True:
        x, y = step(position, direction)
        if x < 0 or x >= cols or y < 0 or y >= rows:
            return False
        if grid[y][x] == "#" or (x, y) == obstacle:
            direction = -direction[1], direction[0]
            continue
        position = x, y
        if (position, direction) in visited:
            return True
        visited.add((position, direction))


@parse_input(parser)
def part1(grid):
    rows = len(grid)
    cols = len(grid[0])
    position = find_guard(grid)
    direction = (0, -1)
    visited = {position}
    while True:
        x, y = step(position, direction)
        if x < 0 or x >= cols or y < 0 or y >= rows:
            return len(visited)
        if grid[y][x] == "#":
            direction = -direction[1], direction[0]
            continue
        position = x, y
        visited.add(position)


@parse_input(parser)
def part2(grid):
    total = 0
    rows = len(grid)
    cols = len(grid[0])
    start_position = find_guard(grid)
    position = start_position
    direction = (0, -1)
    visited = set()
    while True:
        x, y = step(position, direction)
        if x < 0 or x >= cols or y < 0 or y >= rows:
            break
        if grid[y][x] == "#":
            direction = -direction[1], direction[0]
            continue
        if (x, y) not in visited and find_loop(grid, (x, y), position, direction):
            total += 1
        position = x, y
        visited.add(position)
    return total


class Tests202406(unittest.TestCase):
    inputs = (
        "....#.....\n"
        ".........#\n"
        "..........\n"
        "..#.......\n"
        ".......#..\n"
        "..........\n"
        ".#..^.....\n"
        "........#.\n"
        "#.........\n"
        "......#..."
    )

    def test_part1(self):
        expected = 41
        self.assertEqual(expected, part1(self.inputs))

    def test_part2(self):
        expected = 6
        self.assertEqual(expected, part2(self.inputs))


if __name__ == "__main__":
    inputs = import_input()
    print("part 1:", part1(inputs))
    print("part 2:", part2(inputs))
