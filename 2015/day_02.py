# Day 2 of Advent of Code 2015
# I Was Told There Would Be No Math
from aoc.helpers import *

if __name__ == "__main__":
    inputs = [tuple(map(int, dimensions.split("x"))) for dimensions in import_input("\n", example=False)]
    wrapping_paper = 0
    ribbon = 0
    for l, w, h in inputs:
        sides = [(l * w), (w * h), (h * l)]
        slack = min(sides)
        smallest_perimeter = 2 * sum(sorted([l, w, h])[:2])
        surface = 2 * sum(sides)
        volume = l * w * h
        wrapping_paper += surface + slack
        ribbon += smallest_perimeter + volume
    print("total wrapping paper needed:", c(wrapping_paper, 32), "square feet")
    print("total length of ribbon needed:", c(ribbon, 32), "feet")
