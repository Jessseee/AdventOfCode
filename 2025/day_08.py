# Day 08 of Advent of Code 2025
# Playground

import math
import unittest
from collections import Counter
from itertools import combinations, islice
from uuid import uuid4 as uuid

from aoc.helpers import import_input, integers_from_string, timer
from aoc.library.grid import euclidian_distance


@timer(show_result=False)
def parser(inputs):
    junctions = {tuple(integers_from_string(line)) for line in inputs.split("\n")}
    junction_sets = list(combinations(junctions, 2))
    distances = {(junc_a, junc_b): euclidian_distance(junc_a, junc_b) for junc_a, junc_b in junction_sets}
    by_distance = sorted(junction_sets, key=lambda x: distances[x])
    return junctions, by_distance


def connect_junctions(by_distance):
    circuits = {}
    for junc_a, junc_b in by_distance:
        if junc_a in circuits and junc_b in circuits:
            if circuits[junc_a] == circuits[junc_b]:
                pass
            else:
                id_a = circuits[junc_a]
                id_b = circuits[junc_b]
                for key in [key for key, value in circuits.items() if value == id_b]:
                    circuits[key] = id_a
        elif junc_a in circuits:
            id = circuits[junc_a]
            circuits[junc_b] = id
        elif junc_b in circuits:
            id = circuits[junc_b]
            circuits[junc_a] = id
        else:
            id = uuid()
            circuits[junc_a] = id
            circuits[junc_b] = id
        yield circuits, junc_a, junc_b


@timer()
def part1(inputs, n=10):
    _, by_distance = inputs
    circuits, *_ = next(islice(connect_junctions(by_distance), n-1, None))
    return math.prod([x[1] for x in Counter(circuits.values()).most_common(3)])


@timer()
def part2(inputs):
    junctions, by_distance = inputs
    for circuits, junc_a, junc_b in connect_junctions(by_distance):
        if len(set(circuits.values())) == 1 and set(circuits.keys()) == junctions:
            return junc_a[0] * junc_b[0]
    return None


class Tests202508(unittest.TestCase):
    inputs=(
        "162,817,812\n"
        "57,618,57\n"
        "906,360,560\n"
        "592,479,940\n"
        "352,342,300\n"
        "466,668,158\n"
        "542,29,236\n"
        "431,825,988\n"
        "739,650,466\n"
        "52,470,668\n"
        "216,146,977\n"
        "819,987,18\n"
        "117,168,530\n"
        "805,96,715\n"
        "346,949,466\n"
        "970,615,88\n"
        "941,993,340\n"
        "862,61,35\n"
        "984,92,344\n"
        "425,690,689"
    )

    def test_part1(self):
        expected = 40
        self.assertEqual(expected, part1(self.inputs))

    def test_part2(self):
        expected = 25272
        self.assertEqual(expected, part2(self.inputs))


if __name__ == "__main__":
    inputs = import_input(parser=parser)
    part1(inputs, 1000)
    part2(inputs)
