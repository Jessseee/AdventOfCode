# Day 1 of Advent of Code 2017
# Inverse Captcha
from aoc.helpers import *


def solve(interval):
    return sum([inputs[i] for i in range(len(inputs) - 1, -2, -1) if inputs[i] == inputs[i - interval]])


if __name__ == "__main__":
    inputs = import_input("", int)
    print("The captcha with interval 1:", solve(1))
    print("The captcha with interval len/2:", solve(len(inputs) // 2))
