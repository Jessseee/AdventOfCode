# Day 3 of Advent of Code 2018
# <PUZZLE TITLE>

# <PUZZLE DESCRIPTION>

from aoc.helpers import *
from collections import defaultdict


def parse_input(line):
    id, x, y, w, h = list(map(int, re.findall(r"\d+", line)))
    return x, y, x+w, y+h


def overlap(a, b):
    (a_x1, a_y1, a_x2, a_y2), (b_x1, b_y1, b_x2, b_y2) = a, b
    x1, y1, x2, y2 = max(a_x1, b_x1), max(a_y1, b_y1), min(a_x2, b_x2), min(a_y2, b_y2)
    return (x1, y1, x2, y2) if max(0, x2 - x1) * max(0, y2 - y1) else None


if __name__ == '__main__':
    claims = import_input('\n', parse_input, example=False)

    fabric = defaultdict(int)
    for x1, y1, x2, y2 in claims:
        for i in range(y1, y2):
            for j in range(x1, x2):
                fabric[(i, j)] += 1

    print(len([k for k, v in fabric.items() if v > 1]))

    for i in range(len(claims)):
        if not any([overlap(claims[i], claims[j]) for j in range(len(claims)) if i != j]):
            print(i + 1)
            break

