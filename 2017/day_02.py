# Day <DAY> of Advent of Code <YEAR>
# <PUZZLE TITLE>
from itertools import permutations

from aoc.helpers import *

if __name__ == "__main__":
    inputs = [[int(num) for num in row.split("\t")] for row in import_input("\n")]
    print(sum([max(row) - min(row) for row in inputs]))
    print(sum([[comb[0] // comb[1] for comb in permutations(row, 2) if comb[0] % comb[1] == 0][0] for row in inputs]))
