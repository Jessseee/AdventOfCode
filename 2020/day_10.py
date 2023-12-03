# Day 10 Advent of Code
# Matching adapters
import itertools as itr

from aoc.helpers import *


def compare_joltage(index=0, diffs={}):
    if index + 1 < len(adapters):
        diff = adapters[index + 1] - adapters[index]
        if diff in diffs:
            diffs[diff] += 1
        else:
            diffs[diff] = 1
        compare_joltage(index + 1)
    return diffs[1] * diffs[3]


if __name__ == "__main__":
    adapters = [int(i) for i in import_input().read().split("\n")]
    adapters.sort()
    adapters.insert(0, 0)
    adapters.append(max(adapters) + 3)
    print(adapters)
    print(compare_joltage())
