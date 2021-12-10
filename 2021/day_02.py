# Day 2 of Advent of Code 2021
# Dive!

# We found out that the submarine takes commands like `forward 1`, `down 2`, or `up 3`.
# We note that since we're in a submarine, down and up affect your depth,
# and so they have the opposite result of what we might have expected.

from helpers import *
import numpy as np


if __name__ == '__main__':
    inputs = [(dir, int(num)) for dir, num in [line.split(' ') for line in import_input('\n')]]

    # For the first part we assume:
    # - `forward X` increases the horizontal position by X units.
    # - `down X` increases the depth by X units.
    # - `up X` decreases the depth by X units.

    dirs = {'forward': [1, 0], 'up': [0, -1], 'down': [0, 1]}
    pos = np.array([0, 0])
    for dir, num in inputs:
        pos += np.array(dirs[dir]) * np.array([num, num])

    print(f'\nAccording to the {color_text("first", 33)} interpretation of the instructions')
    print(f'The end position of the submarine will be: {color_text(pos, 32)}')
    print(f'The product of these values is: {color_text(pos[0] * pos[1], 32)}')

    # After actually reading the submarines manual we find out the instructions mean something completely different:
    # - `down X` increases your aim by X units.
    # - `up X` decreases your aim by X units.
    # - `forward X` does two things:
    #   - It increases your horizontal position by X units.
    #   - It increases your depth by your aim multiplied by X.

    dirs = {'forward': [0, 1, 1], 'up': [-1, 0, 0], 'down': [1, 0, 0]}
    pos = np.array([0, 0, 0])
    for dir, num in inputs:
        pos += np.array(dirs[dir]) * np.array([num, num, num*pos[0]])

    print(f'\nAccording to the {color_text("second", 33)} interpretation of the instructions')
    print(f'The end position of the submarine will be: {color_text(pos, 32)}')
    print(f'The product of these values is: {color_text(pos[1] * pos[2], 32)}')
