# Day 6 of Advent of Code 2021
# Lanternfish



from helpers import *


if __name__ == '__main__':
    init_fishes = import_input(',', int)
    fishes = [0]*9
    for i in init_fishes:
        fishes[i] += 1

    for day in range(256):
        spawn = fishes.pop(0)
        fishes[6] += spawn
        fishes.append(spawn)
        if day == 79:
            print(f"After {color_text('80', 32)} days there are {color_text('{:,}'.format(sum(fishes)), 31)} angler fish!")
    print(f"After {color_text('256', 32)} days there are {color_text('{:,}'.format(sum(fishes)), 31)} angler fish!")
