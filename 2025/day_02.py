# Day 02 of Advent of Code 2025
# Gift Shop

import re
import unittest

from aoc.helpers import import_input, timer


def parser(inputs):
    return [tuple(map(int, re.findall(r"\d+", input))) for input in inputs.split(",")]


@timer()
def part1(inputs):
    total = 0
    for start, end in inputs:
        for i in range(start, end + 1):
            id = str(i)
            if id[:len(id)//2] == id[len(id)//2:]:
                total += i
    return total


@timer()
def part2(inputs):
    total = 0
    for start, end in inputs:
        for i in range(start, end + 1):
            if re.fullmatch(r"(.+)\1+", str(i)):
                total += i
    return total


class Tests202502(unittest.TestCase):
    inputs = (
        "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,"
        "38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    )

    def test_part1(self):
        expected = 1227775554
        self.assertEqual(expected, part1(self.inputs))

    def test_part2(self):
        expected = 4174379265
        self.assertEqual(expected, part2(self.inputs))


if __name__ == "__main__":
    inputs = import_input(parser=parser)
    part1(inputs)
    part2(inputs)
