# Day 21 of Advent of Code 2024
# Keypad Conundrum

import unittest
from functools import cache

from aoc.helpers import import_input, parse_input


class Keypad:
    def __init__(self, keypad):
        rows, cols = len(keypad), len(keypad[0])
        self.keypad = keypad
        self.positions = {keypad[y][x]: (x, y) for y in range(rows) for x in range(cols)}

    def moves(self, x, y, nx, ny, s=""):
        if (x, y) == (nx, ny):
            yield s + "A"
        if nx < x and self.keypad[y][x - 1] != " ":
            yield from self.moves(x - 1, y, nx, ny, s + "<")
        if ny < y and self.keypad[y - 1][x] != " ":
            yield from self.moves(x, y - 1, nx, ny, s + "^")
        if ny > y and self.keypad[y + 1][x] != " ":
            yield from self.moves(x, y + 1, nx, ny, s + "v")
        if nx > x and self.keypad[y][x + 1] != " ":
            yield from self.moves(x + 1, y, nx, ny, s + ">")

    def sequence(self, current_key, next_key):
        x, y = self.positions[current_key]
        nx, ny = self.positions[next_key]
        return min(self.moves(x, y, nx, ny), key=lambda p: sum(a != b for a, b in zip(p, p[1:])))


NUMERIC_KEYPAD = Keypad([
    ("7", "8", "9"),
    ("4", "5", "6"),
    ("1", "2", "3"),
    (" ", "0", "A")
])

DIRECTIONAL_KEYPAD = Keypad([
    (" ", "^", "A"),
    ("<", "v", ">")
])


@cache
def solve(sequence, max_redirections, cur_redirection=0):
    if cur_redirection > max_redirections:
        return len(sequence)
    keypad = NUMERIC_KEYPAD if cur_redirection == 0 else DIRECTIONAL_KEYPAD
    return sum(
        solve(keypad.sequence(current, next), max_redirections, cur_redirection + 1)
        for current, next in zip("A" + sequence, sequence)
    )


@parse_input(str.split)
def part1(codes):
    return sum(solve(code, 2) * int(code[:-1]) for code in codes)


@parse_input(str.split)
def part2(codes):
    return sum(solve(code, 25) * int(code[:-1]) for code in codes)


class Tests202421(unittest.TestCase):
    inputs = "029A\n980A\n179A\n456A\n379A"

    def test_part1(self):
        expected = 126384
        self.assertEqual(expected, part1(self.inputs))

    def test_part2(self):
        expected = 154115708116294
        self.assertEqual(expected, part2(self.inputs))


if __name__ == "__main__":
    inputs = import_input()
    print("part 1:", part1(inputs))
    print("part 2:", part2(inputs))
