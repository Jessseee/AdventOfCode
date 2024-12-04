# Day 03 of Advent of Code 2024
# Mull It Over
import re
import unittest

from aoc.helpers import import_input


def part1(inputs):
    muls = re.findall(r"mul\((\d+),(\d+)\)", inputs)
    return sum([int(rhs) * int(lhs) for rhs, lhs in muls])


def part2(inputs):
    instructions = re.findall(r"mul\((\d+),(\d+)\)|(do)\(\)|(don't)\(\)", inputs)
    enabled = True
    total = 0
    for instruction in instructions:
        if "do" in instruction:
            enabled = True
        elif "don't" in instruction:
            enabled = False
        elif enabled:
            total += int(instruction[0]) * int(instruction[1])
    return total


class Tests202403(unittest.TestCase):
    def test_part1(self):
        input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        expected = 161
        self.assertEqual(part1(input), expected)

    def test_part2(self):
        input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        expected = 48
        self.assertEqual(part2(input), expected)


if __name__ == "__main__":
    inputs = import_input()
    print("part 1:", part1(inputs))
    print("part 2:", part2(inputs))
