# Day 11 of Advent of Code 2025
# Reactor

import unittest
from functools import cache

from aoc.helpers import import_input, parse_input


def parser(inputs):
    result = {}
    for line in inputs.split("\n"):
        key, value = line.split(": ")
        result[key] = value.split(" ")
    return result


def build_path_counter(inputs):
    @cache
    def iterator(current, target):
        if current == target:
            return 1
        return sum(iterator(neighbour, target) for neighbour in inputs.get(current, []))
    return iterator


@parse_input(parser)
def part1(inputs):
    count_paths = build_path_counter(inputs)
    return count_paths("you", "out")


@parse_input(parser)
def part2(inputs):
    count_paths = build_path_counter(inputs)
    svr_fft = count_paths("svr", "fft")
    fft_dac = count_paths("fft", "dac")
    dac_out = count_paths("dac", "out")

    return svr_fft * fft_dac * dac_out


class Tests202511(unittest.TestCase):
    def test_part1(self):
        inputs = (
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
        inputs = (
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
    inputs = import_input()
    print("part 1:", part1(inputs))
    print("part 2:", part2(inputs))
