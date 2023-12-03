# Day 3 of Advent of Code 2015
# Perfectly Spherical Houses in a Vacuum
from aoc.helpers import *


class Santa:
    def __init__(self):
        self.pos = [0, 0]

    def move(self, direction):
        if direction == "^":
            self.pos[1] += 1
        elif direction == ">":
            self.pos[0] += 1
        elif direction == "v":
            self.pos[1] -= 1
        elif direction == "<":
            self.pos[0] -= 1
        return tuple(self.pos)


if __name__ == "__main__":
    inputs = import_input(example=False).read()
    visited = {(0, 0)}
    real_santa = Santa()
    robo_santa = Santa()
    for i, direction in enumerate(inputs):
        if i % 2 == 0:
            visited.add(real_santa.move(direction))
        else:
            visited.add(robo_santa.move(direction))
    print(len(visited))
