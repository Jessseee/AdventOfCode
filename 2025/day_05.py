# Day 05 of Advent of Code 2025
# Cafeteria

import re
import unittest

from aoc.helpers import import_input, timer


def parser(inputs):
    ranges, ids = map(str.split, inputs.split("\n\n"))
    ranges = sorted([tuple(map(int, re.findall(r"\d+", line))) for line in ranges])
    ranges = [(start, end + 1) for start, end in ranges]  # Make half-open interval
    ids = list(map(int, ids))
    return ranges, ids


@timer()
def part1(inputs):
    total = 0
    ranges, ids = inputs
    for id in ids:
        if any(start <= id < end for start, end in ranges):
            total += 1
    return total


@timer()
def part2(inputs):
    total = 0
    ranges, _ = inputs
    end_points = sorted(set(sum(ranges, ())))  # Flattened sorted list of unique range end-points
    for i in range(len(end_points)-1):
        a, b = end_points[i], end_points[i+1]
        if any(a >= start and b <= end for start, end in ranges):
            total += b - a
    return total


class Tests202505(unittest.TestCase):
    inputs = "3-5\n10-14\n16-20\n12-18\n\n1\n5\n8\n11\n17\n32"

    def test_part1(self):
        expected = 3
        self.assertEqual(expected, part1(self.inputs))

    def test_part2(self):

        expected = 14
        self.assertEqual(expected, part2(self.inputs))


if __name__ == "__main__":
    inputs = import_input(parser=parser)
    part1(inputs)
    part2(inputs)
