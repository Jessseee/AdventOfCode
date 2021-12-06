# Day 6 of Advent of Code 2021
# Lanternfish
from helpers import *


if __name__ == '__main__':
    init_fishes = import_input(',', int)
    fishes = [0]*9
    for i in init_fishes:
        fishes[i] += 1

    print('day', 0, sum(fishes))
    for day in range(256):
        spawn = fishes.pop(0)
        fishes[6] += spawn
        fishes.append(spawn)
        print('day', day+1, sum(fishes))
