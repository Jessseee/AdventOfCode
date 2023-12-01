# Day <DAY> of Advent of Code <YEAR>
# <PUZZLE TITLE>
from helpers import *
import numpy as np
import re
from dataclasses import dataclass


class Screen:
    def __init__(self, rows: int, cols: int,):
        self.screen = np.zeros((rows, cols), int)

    def __str__(self):
        string = ""
        for row in self.screen:
            for col in row:
                string += [". ", "# "][col]
            string += "\n"
        return string

    @dataclass
    class Rect:
        row: int
        col: int

    @dataclass
    class Rotate:
        axis: int
        pos: int
        value: int

    def apply(self, instruction):
        if isinstance(instruction, self.Rect):
            self.apply_rect(instruction)
        elif isinstance(instruction, self.Rotate):
            self.apply_rotate(instruction)

    def apply_rect(self, rect: Rect):
        self.screen[:rect.col, :rect.row] = 1

    def apply_rotate(self, rotate: Rotate):
        if rotate.axis:
            self.screen[rotate.pos, :] = np.roll(self.screen[rotate.pos, :], rotate.value)
        else:
            self.screen[:, rotate.pos] = np.roll(self.screen[:, rotate.pos], rotate.value)


def parse_instructions(line):
    instruction, value = line.split(" ", 1)
    if instruction == "rect":
        x, y = value.split("x")
        return Screen.Rect(int(x), int(y))
    else:
        axis, pos, value = re.findall(r"([x|y])=(\d+) by (\d+)", value)[0]
        return Screen.Rotate(axis == 'y', int(pos), int(value))


if __name__ == '__main__':
    inputs = import_input('\n', parse_instructions, example=False)
    screen = Screen(6, 50)
    for instruction in inputs:
        screen.apply(instruction)
        print(instruction)
        print(screen)
    print("Total pixels lit:", sum(sum(screen.screen)))
