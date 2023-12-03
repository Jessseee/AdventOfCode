# Day <DAY> of Advent of Code <YEAR>
# <PUZZLE TITLE>
from aoc.helpers import *


class Spiral:
    def __init__(self, sum_neighbours=False):
        self.cursor = Vector2D(0, 0)
        self.direction = Vector2D(1, 0)
        self.value = 1
        self.layer = 0
        self.matrix = {(0, 0): 1}
        self.sum_neighbours = sum_neighbours

    def traverse(self, target):
        while self.value < target:
            self.step()
            self.layer += 1
            len_side = 2 * self.layer
            for side in range(4):
                self.direction.rotate90(clockwise=False)
                for steps in range(len_side - (side == 0)):
                    self.step()
                    if self.value >= target:
                        return f"pos: {self.cursor}, value: {self.value}, dist: {self.distance()}"
        return self.distance()

    def distance(self):
        return abs(self.cursor.x) + abs(self.cursor.y)

    def step(self):
        self.cursor += self.direction
        self.value = sum(self.get_neighbours()) if self.sum_neighbours else self.value + 1
        self.matrix[self.cursor] = self.value

    def get_neighbours(self):
        neighbours = []
        for x in range(self.cursor.x - 1, self.cursor.x + 2):
            for y in range(self.cursor.y - 1, self.cursor.y + 2):
                if (x, y) != self.cursor:
                    neighbours.append(self.matrix.get((x, y)) or 0)
        return neighbours


if __name__ == "__main__":
    number = int(import_input(example=False).read())
    print(Spiral(sum_neighbours=False).traverse(number))
    print(Spiral(sum_neighbours=True).traverse(number))


# Step 1: Linear increasing spiral matrix:
#  17   16   15   14   13
#  18    5    4    3   12
#  19    6    1    2   11
#  20    7    8    9   10
#  21   22   23   24   25

# Step 2: Sum filled neighbour spiral matrix:
# 147  142  133  122   59
# 304    5    4    2   57
# 330   10    1    1   54
# 351   11   23   25   26
# 362  747  806  880  931

# Manhattan distance matrix:
#   4    3    2    3    4
#   3    2    1    2    3
#   2    1    0    1    2
#   3    2    1    2    3
#   4    3    2    3    4
