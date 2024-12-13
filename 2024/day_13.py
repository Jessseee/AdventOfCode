# Day 13 of Advent of Code 2024
# Claw Contraption

import re
import unittest

from aoc.helpers import import_input, parse_input


def parser(inputs):
    return [
        [
            tuple(map(int, re.findall(r"(\d+)", line)))
            for line in machine.split("\n")
        ]
        for machine in inputs.split("\n\n")
    ]


@parse_input(parser)
def solve(machines, offset=0):
    total = 0
    for (x1, y1), (x2, y2), (c1, c2) in machines:
        c1, c2 = c1 + offset, c2 + offset
        determinant = x1 * y2 - y1 * x2
        x = (y2 * c1 - x2 * c2) / determinant
        y = (x1 * c2 - y1 * c1) / determinant
        if int(x) == x and int(y) == y:
            total += int(x * 3 + y)
    return total


def part1(inputs):
    return solve(inputs)


def part2(inputs):
    return solve(inputs, 10000000000000)


class Tests202413(unittest.TestCase):
    inputs = (
        "Button A: X+94, Y+34\n"
        "Button B: X+22, Y+67\n"
        "Prize: X=8400, Y=5400\n"
        "\n"
        "Button A: X+26, Y+66\n"
        "Button B: X+67, Y+21\n"
        "Prize: X=12748, Y=12176\n"
        "\n"
        "Button A: X+17, Y+86\n"
        "Button B: X+84, Y+37\n"
        "Prize: X=7870, Y=6450\n"
        "\n"
        "Button A: X+69, Y+23\n"
        "Button B: X+27, Y+71\n"
        "Prize: X=18641, Y=10279"
    )

    def test_part1(self):
        expected = 480
        self.assertEqual(expected, part1(self.inputs))

    def test_part2(self):
        expected = None
        self.assertEqual(expected, part2(self.inputs))


if __name__ == "__main__":
    inputs = import_input()
    print("part 1:", part1(inputs))
    print("part 2:", part2(inputs))
