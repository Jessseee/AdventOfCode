# Day 18 of Advent of Code 2024
# RAM Run

import heapq
import re
import unittest
from math import inf

from aoc.helpers import (
    import_input,
    parse_input,
    reconstruct_path,
    get_neighbours_within_bound,
)


def parser(inputs):
    return [tuple(map(int, re.findall(r"\d+", line))) for line in inputs.split("\n")]


def find_path(size, corruptions):
    start, target = (0, 0), (size, size)
    heapq.heappush(to_visit := [], (0, start))
    g_score = {start: 0}
    connections = {}

    while len(to_visit) > 0:
        current_g_score, current = heapq.heappop(to_visit)
        if current == target:
            return reconstruct_path(connections, current, target)
        for neighbour in get_neighbours_within_bound(*current, max_x=size+1, max_y=size+1):
            if neighbour in corruptions:
                continue
            tentative_g_score = current_g_score + 1
            if tentative_g_score < g_score.get(neighbour, inf):
                connections[neighbour] = current
                g_score[neighbour] = tentative_g_score
                heapq.heappush(to_visit, (tentative_g_score, neighbour))


@parse_input(parser)
def part1(inputs, size, n_bytes):
    corruptions = inputs[:n_bytes]
    path = find_path(size, corruptions)
    return len(path) - 1


@parse_input(parser)
def part2(inputs, size):
    i = len(inputs)
    while (i := i - 1) > 0:
        if find_path(size, inputs[:i]):
            return inputs[i]


class Tests202418(unittest.TestCase):
    inputs = ("5,4\n4,2\n4,5\n3,0\n2,1\n6,3\n2,4\n1,5\n0,6\n3,3\n2,6\n5,1\n"
              "1,2\n5,5\n2,5\n6,5\n1,4\n0,4\n6,4\n1,1\n6,1\n1,0\n0,5\n1,6\n2,0")

    def test_part1(self):
        expected = 22
        self.assertEqual(expected, part1(self.inputs, 6, 12))

    def test_part2(self):
        expected = (6, 1)
        self.assertEqual(expected, part2(self.inputs, 6))


if __name__ == "__main__":
    inputs = import_input()
    print("part 1:", part1(inputs, 70, 1024))
    print("part 2:", part2(inputs, 70))
