# Day 25 of Advent of Code 2024
# Code Chronicle

import unittest

from aoc.helpers import import_input, parse_input


def parser(inputs):
    keys, locks = [], []
    for input in inputs.split("\n\n"):
        input = [list(map(lambda x: x == "#", row)) for row in input.split("\n")]
        is_lock = all(input[0])
        rows, cols = len(input), len(input[0])
        input = [sum(input[y][x] for y in range(rows)) - 1 for x in range(cols)]
        if is_lock:
            locks.append(input)
        else:
            keys.append(input)
    return keys, locks


@parse_input(parser)
def part1(inputs):
    keys, locks = inputs
    return sum(
        not any(a + b > 5 for a, b in zip(key, lock))
        for key in keys
        for lock in locks
    )


class Tests202425(unittest.TestCase):
    def test_part1(self):
        inputs = (
            "#####\n"
            ".####\n"
            ".####\n"
            ".####\n"
            ".#.#.\n"
            ".#...\n"
            ".....\n"
            "\n"
            "#####\n"
            "##.##\n"
            ".#.##\n"
            "...##\n"
            "...#.\n"
            "...#.\n"
            ".....\n"
            "\n"
            ".....\n"
            "#....\n"
            "#....\n"
            "#...#\n"
            "#.#.#\n"
            "#.###\n"
            "#####\n"
            "\n"
            ".....\n"
            ".....\n"
            "#.#..\n"
            "###..\n"
            "###.#\n"
            "###.#\n"
            "#####\n"
            "\n"
            ".....\n"
            ".....\n"
            ".....\n"
            "#....\n"
            "#.#..\n"
            "#.#.#\n"
            "#####"
        )
        expected = 3
        self.assertEqual(expected, part1(inputs))


if __name__ == "__main__":
    inputs = import_input()
    print("part 1:", part1(inputs))
    print("part 2: HAPPY CHRISTMAS")
