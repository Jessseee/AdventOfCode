# Day 2 of Advent of Code 2018
# <PUZZLE TITLE>

# <PUZZLE DESCRIPTION>

from aoc.helpers import *
from collections import Counter
from itertools import combinations


def n_of_letter(n, ids):
    return [any([k for k, v in Counter(id).items() if v == n]) for id in ids]


if __name__ == '__main__':
    ids = import_input('\n', example=False)
    print(sum(n_of_letter(2, ids)) * sum(n_of_letter(3, ids)))

    for a, b in combinations(ids, 2):
        diff = [a[i] for i in range(len(a)) if a[i] == b[i]]
        if len(a) - len(diff) == 1:
            print("".join(diff))
            break


