# Day 09 of Advent of Code 2025
# Movie Theater

import unittest
from itertools import combinations

from aoc.helpers import import_input, integers_from_string, timer


def parser(inputs):
    return [tuple(integers_from_string(line)) for line in inputs.split("\n")]


def rect_area(a, b):
    (x1, y1), (x2, y2) = a, b
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


@timer()
def part1(inputs):
    return max(rect_area(a, b) for a, b in combinations(inputs, 2))


@timer()
def part2(inputs):
    edges = []
    for i in range(len(inputs)):
        (x1, y1), (x2, y2) = inputs[i], inputs[(i + 1) % len(inputs)]
        edges.append((min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)))

    def rect_collide_with_edges(rect):
        """AABB collision to check if any edge is within a rectangle."""
        r_min_x, r_min_y, r_max_x, r_max_y = rect
        for edge in edges:
            e_min_x, e_min_y, e_max_x, e_max_y = edge
            if r_min_x < e_max_x and r_max_x > e_min_x and r_min_y < e_max_y and r_max_y > e_min_y:
                return True
        return False

    rects = sorted([(a, b, rect_area(a, b)) for a, b in combinations(inputs, 2)], key=lambda x: x[2], reverse=True)
    for (x1, y1), (x2, y2), area in rects:
        rect = (min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
        if not rect_collide_with_edges(rect):
            return area
    return None


class Tests202509(unittest.TestCase):
    inputs = "7,1\n11,1\n11,7\n9,7\n9,5\n2,5\n2,3\n7,3"

    def test_part1(self):
        expected = 50
        self.assertEqual(expected, part1(self.inputs))

    def test_part2(self):
        expected = 24
        self.assertEqual(expected, part2(self.inputs))


if __name__ == "__main__":
    inputs = import_input(parser=parser)
    part1(inputs)
    part2(inputs)
