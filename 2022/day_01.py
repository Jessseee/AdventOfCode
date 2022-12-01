# Day 1 of Advent of Code 2022
# Calorie Counting

# To collect star fruit for Santa's reindeer the elves must go on an expedition into the grove
# where this magical fruit can be plucked. On this expedition the elves each bring a number of snacks,
# it is important that they eat enough calories to survive the expedition. Our task is to make an
# inventory of all the snacks the elves have brought and find which elves carry the most calories.

from helpers import *


def sum_calories(snacks):
    return sum(map(int, snacks.split('\n')))


if __name__ == '__main__':
    elves = import_input('\n\n', sum_calories, example=False)
    ranked = sorted(elves, reverse=True)

    print(f"The top elf carries {color_text(ranked[0], Color.GREEN)} calories.")
    print(f"The top three elves carry {color_text(sum(ranked[:3]), Color.GREEN)} calories.")
