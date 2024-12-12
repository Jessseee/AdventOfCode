# Day 12 of Advent of Code 2024
# Garden Groups

import unittest

from aoc.helpers import import_input, parse_input


def solve(grid) -> (set[int], set[(int, int, int, int)]):
    rows, cols = len(grid), len(grid[0])
    regions = []
    unvisited = set((x, y) for x in range(cols) for y in range(rows))
    while len(unvisited) > 0:
        x, y = unvisited.pop()
        type = grid[y][x]
        to_visit = [(x, y)]
        region = {(x, y)}
        fences = set()
        while len(to_visit) > 0:
            x, y = to_visit.pop()
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= cols or ny < 0 or ny >= rows or grid[ny][nx] != type:
                    fences.add((nx, ny, dx, dy))
                    continue
                if (nx, ny) not in region:
                    region.add((nx, ny))
                    to_visit.append((nx, ny))
        unvisited -= region
        regions.append((region, fences))
    return regions


@parse_input(lambda grid: [list(row) for row in grid.split("\n")])
def part1(grid):
    return sum([len(region) * len(fences) for region, fences in solve(grid)])


@parse_input(lambda grid: [list(row) for row in grid.split("\n")])
def part2(grid):
    total = 0
    for region, fences in solve(grid):
        area = len(region)
        sides = len(fences)
        for x, y, dx, dy in fences:
            if (x - 1, y, dx, dy) in fences or (x, y - 1, dx, dy) in fences:
                sides -= 1
        total += area * sides
    return total


class Tests202412(unittest.TestCase):
    inputs = (
        "RRRRIICCFF\n"
        "RRRRIICCCF\n"
        "VVRRRCCFFF\n"
        "VVRCCCJFFF\n"
        "VVVVCJJCFE\n"
        "VVIVCCJJEE\n"
        "VVIIICJJEE\n"
        "MIIIIIJJEE\n"
        "MIIISIJEEE\n"
        "MMMISSJEEE"
    )

    def test_part1(self):
        expected = 1930
        self.assertEqual(expected, part1(self.inputs))

    def test_part2(self):
        expected = 1206
        self.assertEqual(expected, part2(self.inputs))


if __name__ == "__main__":
    inputs = import_input()
    print("part 1:", part1(inputs))
    print("part 2:", part2(inputs))
