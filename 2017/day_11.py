# Day <DAY> of Advent of Code <YEAR>
# <PUZZLE TITLE>
from aoc.helpers import *


def distance(pos):
    return (abs(pos[0]) + abs(pos[0] + pos[1]) + abs(pos[1])) // 2


directions = hexagonal_directions(as_dict=True)

if __name__ == "__main__":
    paths = import_input("\n")
    for path in paths:
        path = path.split(",")
        position = (0, 0)
        distances = []
        print("\t", 0, position)
        for direction in path:
            position = add_tuples(position, directions[direction])
            dist = distance(position)
            distances.append(dist)
            print(direction, "\t", dist, position)
        print(f"The shortest path is {c(distances[-1], 32)} tiles long.")
        print(f"The furthest distance recorded was {c(max(distances), 32)} tiles away.")
