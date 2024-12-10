# Day 10 of Advent of Code 2024
# Hoof It

import unittest

from aoc.helpers import import_input, parse_input, get_neighbours_within_bound


def parser(grid):
    grid = [list(map(int, row)) for row in grid.split("\n")]
    rows = len(grid)
    cols = len(grid[0])
    trail_heads = []
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == 0:
                trail_heads.append((x, y))
    return grid, rows, cols, trail_heads


@parse_input(parser)
def part1(inputs):
    grid, rows, cols, trail_heads = inputs
    total = 0
    for start in trail_heads:
        to_visit = [start]
        explored = set(start)
        while len(to_visit):
            x, y = current = to_visit.pop()
            if grid[y][x] == 9:
                total += 1
            for neighbour in get_neighbours_within_bound(*current, max_x=cols, max_y=rows):
                nx, ny = neighbour
                if neighbour not in explored and grid[ny][nx] == grid[y][x] + 1:
                    explored.add(neighbour)
                    to_visit.append(neighbour)
    return total


@parse_input(parser)
def part2(inputs):
    grid, rows, cols, trail_heads = inputs
    total = 0
    for start in trail_heads:
        to_visit = [start]
        while len(to_visit):
            x, y = current = to_visit.pop()
            if grid[y][x] == 9:
                total += 1
            for neighbour in get_neighbours_within_bound(*current, max_x=cols, max_y=rows):
                nx, ny = neighbour
                if grid[ny][nx] == grid[y][x] + 1:
                    to_visit.append(neighbour)
    return total


class Tests202410(unittest.TestCase):
    inputs = (
        "89010123\n"
        "78121874\n"
        "87430965\n"
        "96549874\n"
        "45678903\n"
        "32019012\n"
        "01329801\n"
        "10456732"
    )

    def test_part1(self):
        expected = 36
        self.assertEqual(expected, part1(self.inputs))

    def test_part2(self):
        expected = 81
        self.assertEqual(expected, part2(self.inputs))


if __name__ == "__main__":
    inputs = import_input()
    print("part 1:", part1(inputs))
    print("part 2:", part2(inputs))
