# Day 02 of Advent of Code 2024
# Red-Nosed Reports

import unittest

from aoc.helpers import import_input, parse_input, c, Color


def parser(inputs: str):
    return [list(map(int, line.split())) for line in inputs.split("\n")]


def increasing(i, j):
    return 1 <= abs(i - j) <= 3 and i - j > 0


def decreasing(i, j):
    return 1 <= abs(i - j) <= 3 and i - j < 0


def check_report(report):
    diffs = list(zip(report, report[1:]))
    return all(increasing(i, j) for i, j in diffs) or all(decreasing(i, j) for i, j in diffs)


def check_report_with_problem_dampener(report):
    for i in range(len(report)):
        new_report = report.copy()
        new_report.pop(i)
        diffs = list(zip(new_report, new_report[1:]))
        if all(increasing(i, j) for i, j in diffs) or all(decreasing(i, j) for i, j in diffs):
            return True
    return False


@parse_input(parser)
def part1(inputs):
    return sum(map(check_report, inputs))


@parse_input(parser)
def part2(inputs):
    return sum(map(check_report_with_problem_dampener, inputs))


class Tests202402(unittest.TestCase):
    def test_part1(self):
        input = ("7 6 4 2 1\n"  # Safe because the levels are all decreasing by 1 or 2.
                 "1 2 7 8 9\n"  # Unsafe because 2 7 is an increase of 5.
                 "9 7 6 2 1\n"  # Unsafe because 6 2 is a decrease of 4.
                 "1 3 2 4 5\n"  # Unsafe because 1 3 is increasing but 3 2 is decreasing.
                 "8 6 4 4 1\n"  # Unsafe because 4 4 is neither an increase nor a decrease.
                 "1 3 6 7 9")   # Safe because the levels are all increasing by 1, 2, or 3.
        expected = 2
        self.assertEqual(expected, part1(input))

    def test_part2(self):
        # List of edge cases: https://www.reddit.com/r/adventofcode/comments/1h4shdu/2024_day_2_part2_edge_case_finder/
        input = ("48 46 47 49 51 54 56\n"
                 "1 1 2 3 4 5\n"
                 "1 2 3 4 5 5\n"
                 "5 1 2 3 4 5\n"
                 "1 4 3 2 1\n"
                 "1 6 7 8 9\n"
                 "1 2 3 4 3\n"
                 "9 8 7 6 7\n"
                 "7 10 8 10 11\n"
                 "29 28 27 25 26 25 22 20")
        expected = 10
        self.assertEqual(expected, part2(input))


if __name__ == "__main__":
    inputs = import_input()
    print("part 1:", part1(inputs))
    print("part 2:", part2(inputs))
