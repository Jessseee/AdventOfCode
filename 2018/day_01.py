# Day 01 of Advent of Code 2018
# <PUZZLE TITLE>

# <PUZZLE DESCRIPTION>

from aoc.helpers import *
from itertools import accumulate, cycle


if __name__ == '__main__':
    inputs = import_input('\n', int, example=False)
    freqs = set()
    first_repeat = next(freq for freq in accumulate(cycle(inputs)) if freq in freqs or freqs.add(freq))
    print("Frequency after one iteration:", sum(inputs))
    print("First repeating frequency:", first_repeat)

