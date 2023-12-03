# Day <DAY> of Advent of Code <YEAR>
# <PUZZLE TITLE>
from aoc.helpers import *


def parse_discs(line):
    pattern = r"Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+)."
    return list(map(int, re.search(pattern, line).groups()))


if __name__ == "__main__":
    discs = import_input("\n", parse_discs, example=False)
    discs.append([len(discs) + 1, 11, 0])
    i = 0
    while any([(i + disc[0] + disc[2]) % disc[1] for disc in discs]):
        i += 1
    print(f"The perfect time to drop the ball is at time={i}")
