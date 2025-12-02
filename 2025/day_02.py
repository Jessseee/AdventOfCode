# Day 02 of Advent of Code 2025
# Gift Shop

import re
import unittest

from aoc.helpers import import_input, parse_input


def parse(inputs):
    return [tuple(map(int, re.findall(r"\d+", input))) for input in inputs.split(",")]


@parse_input(parse)
def part1(inputs):
    total = 0
    for start, end in inputs:
        for i in range(start, end + 1):
            id = str(i)
            if id[:len(id)//2] == id[len(id)//2:]:
                total += i
    return total


@parse_input(parse)
def part2(inputs):
    total = 0
    for start, end in inputs:
        for i in range(start, end + 1):
            id = str(i)
            for j in range(1, len(id)//2 + 1):
                if re.match(f"({id[:j]})*$", id):
                    total += i
                    break
    return total


class Tests202502(unittest.TestCase):
    def test_part1(self):
        inputs = ("11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,"
                  "38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124")
        expected = 1227775554
        self.assertEqual(expected, part1(inputs))

    def test_part2(self):
        inputs = ("11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,"
                  "38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124")
        expected = 4174379265
        self.assertEqual(expected, part2(inputs))


if __name__ == "__main__":
    inputs = import_input()
    print("part 1:", part1(inputs))
    print("part 2:", part2(inputs))
