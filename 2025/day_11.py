# Day 11 of Advent of Code 2025
# Reactor

import unittest
from functools import cache

from aoc.helpers import import_input, timer


def parser(inputs):
    result = {}
    for line in inputs.split("\n"):
        key, value = line.split(": ")
        result[key] = value.split(" ")
    return result


@timer()
def part1(inputs):
    @cache
    def count_paths(current, target):
        if current == target:
            return 1
        return sum(count_paths(neighbour, target) for neighbour in inputs.get(current, []))

    return count_paths("you", "out")


@timer()
def part2(inputs):
    @cache
    def count_paths(current, target, flag=0):
        if current == "fft" or current == "dac":
            flag += 1
        if current == target:
            return int(flag == 2)
        return sum(count_paths(neighbour, target, flag) for neighbour in inputs.get(current, []))

    return count_paths("svr", "out")


class Tests202511(unittest.TestCase):
    def test_part1(self):
        inputs = parser(
            "aaa: you hhh\n"
            "you: bbb ccc\n"
            "bbb: ddd eee\n"
            "ccc: ddd eee fff\n"
            "ddd: ggg\n"
            "eee: out\n"
            "fff: out\n"
            "ggg: out\n"
            "hhh: ccc fff iii\n"
            "iii: out"
        )
        expected = 5
        self.assertEqual(expected, part1(inputs))

    def test_part2(self):
        inputs = parser(
            "svr: aaa bbb\n"
            "aaa: fft\n"
            "fft: ccc\n"
            "bbb: tty\n"
            "tty: ccc\n"
            "ccc: ddd eee\n"
            "ddd: hub\n"
            "hub: fff\n"
            "eee: dac\n"
            "dac: fff\n"
            "fff: ggg hhh\n"
            "ggg: out\n"
            "hhh: out"
        )
        expected = 2
        self.assertEqual(expected, part2(inputs))


if __name__ == "__main__":
    inputs = import_input(parser=parser)
    part1(inputs)
    part2(inputs)
