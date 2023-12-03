# Day 4 of Advent of Code 2022
# Camp Cleanup

# Before continuing on the camp needs to be cleaned up. Several Elves have been
# assigned to clean sections of the camp in pairs. Each Elf is assigned a part
# of the camp by a range of the camp section ID numbers. However, as the Elves
# compare their section assignment they noticed that many overlap or even contain
# all the other's sections. Our job is to find these section assignments that
# overlap or contain each other from a list of section assignment pairs.

import re

from aoc.helpers import *


def contains(sections1, sections2):
    return in_range(sections1[0], sections2) and in_range(sections1[1], sections2)


def overlaps(sections1, sections2):
    return in_range(sections1[0], sections2) or in_range(sections1[1], sections2)


def in_range(n, range):
    return range[0] <= n <= range[1]


def get_pairs(line):
    pattern = re.compile(r"(\d+-\d+)")
    pair = re.findall(pattern, line)
    return [list(map(int, assignment.split("-"))) for assignment in pair]


if __name__ == "__main__":
    pairs = import_input("\n", get_pairs, example=False)
    contained = 0
    overlapped = 0
    for pair in pairs:
        if contains(pair[0], pair[1]) or contains(pair[1], pair[0]):
            contained += 1
        if overlaps(pair[0], pair[1]) or overlaps(pair[1], pair[0]):
            overlapped += 1
    print(f"{c(contained, Color.GREEN)} section assignments are contained in that of their cleaning partner.")
    print(f"{c(overlapped, Color.GREEN)} section assignments overlap with that of their cleaning partner.")
