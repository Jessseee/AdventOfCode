# Day 11 of Advent of Code 2024
# Plutonian Pebbles

import unittest
from functools import cache
from math import floor, log10

from aoc.helpers import import_input, parse_input


@cache
def change(stone, depth):
    if depth == 0:
        return 1
    depth -= 1
    if stone == 0:
        return change(1, depth)
    digits = floor(log10(stone)) + 1
    if digits % 2 == 0:
        left = stone // 10 ** (digits // 2)
        right = stone - left * 10 ** (digits // 2)
        return change(left, depth) + change(right, depth)
    return change(stone * 2024, depth)


def solve(stones, blinks):
    return sum(change(stone, blinks) for stone in stones)


def parser(stones):
    return map(int, stones.split())


@parse_input(parser)
def part1(stones):
    return solve(stones, 25)


@parse_input(parser)
def part2(stones):
    return solve(stones, 75)


class Tests202411(unittest.TestCase):
    def test_part1(self):
        inputs = "125 17"
        expected = 55312
        self.assertEqual(expected, part1(inputs))

    def test_part2(self):
        inputs = "125 17"
        expected = 65601038650482
        self.assertEqual(expected, part2(inputs))


if __name__ == "__main__":
    inputs = import_input()
    print("part 1:", part1(inputs))
    print("part 2:", part2(inputs))
