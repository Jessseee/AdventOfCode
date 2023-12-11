# Day 11 of Advent of Code 2023
# Cosmic Expansion

# Continuing our journey to the Hot Springs we come across an observatory. The Elf running
# the observatory is studying cosmic expansion using the giant telescope. He does not know
# anything about the missing machine parts, but he can point us towards the Hot Springs if
# we can help him with today's observation analysis. Our task is to calculate the distance
# between stars taking into account an amount of cosmic expansion in the empty space between.

from itertools import combinations

import numpy as np

from aoc.helpers import *


def get_expansion(star_map, expansion):
    space_map = np.ones(star_map.shape, dtype=int)
    empty_rows = np.array([i for i, row in enumerate(star_map[:]) if not row.any()])
    empty_cols = np.array([i for i, col in enumerate(star_map.T[:]) if not col.any()])
    space_map[empty_rows] = expansion
    space_map[:, empty_cols] = expansion
    return space_map


def get_stars(star_map, expansion):
    space_map = get_expansion(star_map, expansion)
    stars = [(sum(space_map[:row, col]), sum(space_map[row, :col])) for row, col in np.argwhere(star_map)]
    return stars


def sum_distances(stars):
    distance = np.int64()
    for star1, star2 in combinations(stars, 2):
        distance += manhattan_distance(star1, star2)
    return distance


if __name__ == "__main__":
    star_map = np.array(import_input("\n", lambda row: [x == "#" for x in row]))

    print(
        "Sum of the distance between all stars (small expansion):    ",
        c(sum_distances(get_stars(star_map, 2)), Color.GREEN),
    )
    print(
        "Sum of the distance between all stars (large expansion):",
        c(sum_distances(get_stars(star_map, 100000)), Color.GREEN),
    )
