# Day 12 of Advent of Code 2025
# Christmas Tree Farm

import numpy as np

from aoc.helpers import import_input, integers_from_string, timer


def parser(inputs):
    *shapes, regions = inputs.split("\n\n")
    shapes = [np.array(list([np.array(list(row)) == '#' for row in shape.split("\n")[1:]])) for shape in shapes]
    regions = [((w, h), [(shapes[i], n) for i, n in enumerate(to_pack) if n > 0]) for w, h, *to_pack in map(integers_from_string, regions.split("\n"))]
    return regions


@timer()
def part1(inputs):
    return sum(w * h >= sum([np.sum(shape) * n for shape, n in shapes_to_pack]) for (w, h), shapes_to_pack in inputs)


if __name__ == "__main__":
    inputs = import_input(parser=parser)
    print("part 1:", part1(inputs))
