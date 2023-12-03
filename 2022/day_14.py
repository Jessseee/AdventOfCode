# Day 14 of Advent of Code 2022
# Regolith Reservoir

# The distress signal seems to come from a cave system hidden behind a waterfall. However, when we enter the
# caves the ground starts rumbling and sand starts flowing into the cave. Our job is to find out where the
# sand will settle down.

from enum import IntEnum
from math import inf

import matplotlib.pyplot as plt
import numpy as np

from aoc.helpers import *


class Cell(IntEnum):
    EMPTY = 0
    SAND = 1
    ROCK = 2


class Cave:
    def __init__(self, paths, floor=False):
        col_min = inf
        col_max = row_max = 0
        for path in paths:
            for point in path:
                col_min = min(col_min, point[0])
                col_max = max(col_max, point[0])
                row_max = max(row_max, point[1])

        col_min -= row_max
        col_max += row_max
        row_max += 2

        self.cells = np.zeros((row_max + 1, col_max - col_min), int)
        for path in paths:
            for i in range(1, len(path)):
                p1 = {"col": path[i - 1][0] - col_min, "row": path[i - 1][1] + 1}
                p2 = {"col": path[i][0] - col_min, "row": path[i][1] + 1}
                for col in range(min(p1["col"], p2["col"]) - 1, max(p1["col"], p2["col"])):
                    for row in range(min(p1["row"], p2["row"]) - 1, max(p1["row"], p2["row"])):
                        self.cells[row, col] = Cell.ROCK
        if floor:
            self.cells[row_max, :] = Cell.ROCK

        self.col_min, self.col_max, self.row_max = col_min, col_max, row_max
        self.sand = [self.new_grain()]

    def new_grain(self):
        return {"col": 500 - self.col_min - 1, "row": 0}

    def drop_sand(self):
        while True:
            grain = self.sand[-1]
            next_pos = {"col": grain["col"], "row": grain["row"] + 1}
            self.cells[grain["row"], grain["col"]] = 0
            if next_pos["row"] > self.row_max:
                return self.finish()
            elif self.cells[next_pos["row"], next_pos["col"]] == Cell.EMPTY:
                grain["row"] += 1
            elif self.cells[next_pos["row"], next_pos["col"] - 1] == Cell.EMPTY:
                grain["col"] -= 1
                grain["row"] += 1
            elif self.cells[next_pos["row"], next_pos["col"] + 1] == Cell.EMPTY:
                grain["col"] += 1
                grain["row"] += 1
            else:
                self.cells[grain["row"], grain["col"]] = Cell.SAND
                self.sand.append(self.new_grain())
                if self.sand[-1] == self.sand[-2]:
                    return self.finish()
            self.cells[grain["row"], grain["col"]] = Cell.SAND

    def finish(self):
        plt.imshow(self.cells)
        plt.axis("off")
        plt.show()
        return len(self.sand) - 1


def parse_path(path):
    return [list(map(int, point.split(","))) for point in path.split(" -> ")]


if __name__ == "__main__":
    paths = import_input("\n", parse_path, example=True)

    cave = Cave(paths, False)
    print(f"{cave.drop_sand()} grains of sand have come to rest (without floor).")
    cave = Cave(paths, True)
    print(f"{cave.drop_sand()} grains of sand have come to rest (with floor).")
