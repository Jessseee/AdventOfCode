# Day 3 of Advent of Code 2022
# Rucksack Reorganization

# Unfortunately, one elf did not follow the instruction while packing the rucksacks
# for the expedition, so they have to be rearranged. Each rucksack has two equally sized
# compartments, each rucksack should only contain one item of any type. Each item
# type is identified by a single lower- or uppercase letter (a-Z). Our job is to find
# any packing errors and score them according to their type (a: 1 - Z: 52). After we
# finish finding errors we also need to find which item types correspond to group badges.
# These can be found as an item which is common between a group of three rucksacks.

import string

from aoc.helpers import *


def compartmentalize(rucksack):
    """
    Split rucksack item list into two compartments.

    @param rucksack: The rucksack item list to split.
    @return: Split rucksack item list.
    """
    divide = len(rucksack) // 2
    return [rucksack[:divide], rucksack[divide:]]


def compare_rucksacks(all_rucksacks, n=1):
    """
    Compare groups of rucksacks for common items.

    @param all_rucksacks: List of all rucksacks.
    @param n: Size of groups. If n=1, then compare compartments.
    @return: Total score of common items.
    """
    scores = list(string.ascii_letters)
    score = 0
    for i in range(0, len(all_rucksacks), n):
        if n == 1:
            rucksacks = compartmentalize(all_rucksacks[i])
        else:
            rucksacks = all_rucksacks[i : i + n]
        for item in rucksacks[0]:
            if all([item in rucksack for rucksack in rucksacks[1:]]):
                score += scores.index(item) + 1
                break
    return score


if __name__ == "__main__":
    rucksacks = import_input("\n", example=False)

    print("Score of common items in rucksack compartments: ", c(compare_rucksacks(rucksacks, 1), Color.GREEN))

    print("Score of common items in groups of three rucksacks: ", c(compare_rucksacks(rucksacks, 3), Color.GREEN))
