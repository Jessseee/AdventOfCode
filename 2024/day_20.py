# Day 20 of Advent of Code 2024
# Race Condition

import unittest

from aoc.helpers import import_input, parse_input


def get_path(grid, start, target):
    path = {start: 0}
    steps = 1
    previous = None
    current = start
    while current != target:
        x, y = current
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            nx, ny = next = x + dx, y + dy
            if grid[ny][nx] == "#" or next == previous:
                continue
            previous = current
            current = next
            path[current] = steps
            break
        steps += 1
    return path


def parser(grid):
    grid = [list(row) for row in grid.split("\n")]
    start, target = None, None
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "S":
                start = (x, y)
            if cell == "E":
                target = (x, y)
            if start and target:
                break
    return get_path(grid, start, target)


def solve(path, min_savings, cheat_distance):
    total = 0
    for current in path:
        x, y = current
        for dx in range(-cheat_distance, cheat_distance + 1):
            for dy in range(-cheat_distance + abs(dx), cheat_distance + 1 - abs(dx)):
                next = x + dx, y + dy
                if next in path:
                    saving = path[next] - path[current] - (abs(dx) + abs(dy))
                    if saving >= min_savings:
                        total += 1
    return total


@parse_input(parser)
def part1(path, min_savings):
    return solve(path, min_savings, 2)


@parse_input(parser)
def part2(path, min_savings):
    return solve(path, min_savings, 20)


class Tests202420(unittest.TestCase):
    inputs = (
        "###############\n"
        "#...#...#.....#\n"
        "#.#.#.#.#.###.#\n"
        "#S#...#.#.#...#\n"
        "#######.#.#.###\n"
        "#######.#.#...#\n"
        "#######.#.###.#\n"
        "###..E#...#...#\n"
        "###.#######.###\n"
        "#...###...#...#\n"
        "#.#####.#.###.#\n"
        "#.#...#.#.#...#\n"
        "#.#.#.#.#.#.###\n"
        "#...#...#...###\n"
        "###############"
    )

    def test_part1(self):
        expected = 44
        self.assertEqual(expected, part1(self.inputs, 1))

    def test_part2(self):
        expected = 285
        self.assertEqual(expected, part2(self.inputs, 50))


if __name__ == "__main__":
    inputs = import_input()
    print("part 1:", part1(inputs, 100))
    print("part 2:", part2(inputs, 100))
