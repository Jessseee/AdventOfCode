# Day 04 of Advent of Code 2024
# Ceres Search

import unittest

from aoc.helpers import import_input


def part1(inputs):
    word = "XMAS"
    total = 0
    grid = inputs.split("\n")
    max_rows, max_cols = len(grid), len(grid[0])
    for row in range(max_rows):
        for col in range(max_cols):
            for dx, dy in [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]:
                for i in range(len(word)):
                    y, x = row+dy*i, col+dx*i
                    if (x < 0 or x >= max_cols) or (y < 0 or y >= max_rows):
                        break
                    if grid[y][x] != word[i]:
                        break
                    if i == len(word) - 1:
                        total += 1
    return total


def neighbours(row, col):
    return [(row + dy, col + dx) for dx, dy in [(-1, 1), (1, -1), (1, 1), (-1, -1)]]


def part2(inputs):
    total = 0
    grid = inputs.split("\n")
    max_rows, max_cols = len(grid), len(grid[0])
    for row in range(1, max_rows-1):
        for col in range(1, max_cols-1):
            if grid[row][col] != "A":
                continue
            (x1, y1), (x2, y2), (x3, y3), (x4, y4) = neighbours(row, col)
            if (((grid[y1][x1] == "M" and grid[y2][x2] == "S") or (grid[y1][x1] == "S" and grid[y2][x2] == "M")) and
               ((grid[y3][x3] == "M" and grid[y4][x4] == "S") or (grid[y3][x3] == "S" and grid[y4][x4] == "M"))):
                total += 1
    return total


class Tests202404(unittest.TestCase):
    inputs = (
        "MMMSXXMASM\n"
        "MSAMXMSMSA\n"
        "AMXSXMAAMM\n"
        "MSAMASMSMX\n"
        "XMASAMXAMM\n"
        "XXAMMXXAMA\n"
        "SMSMSASXSS\n"
        "SAXAMASAAA\n"
        "MAMMMXMMMM\n"
        "MXMXAXMASX"
    )

    def test_part1(self):
        expected = 18
        self.assertEqual(expected, part1(self.inputs))

    def test_part2(self):
        expected = 9
        self.assertEqual(expected, part2(self.inputs))


if __name__ == "__main__":
    inputs = import_input()
    print("part 1:", part1(inputs))
    print("part 2:", part2(inputs))
