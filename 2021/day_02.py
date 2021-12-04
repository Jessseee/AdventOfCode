from helpers import *
import numpy as np


if __name__ == '__main__':
    inputs = [(dir, int(num)) for dir, num in [line.split(' ') for line in import_input().read().split('\n')]]

    dirs = {'forward': [1, 0], 'up': [0, -1], 'down': [0, 1]}
    pos = np.array([0, 0])
    for dir, num in inputs:
        pos += np.array(dirs[dir]) * np.array([num, num])

    print(f'\nAccording to the {color_text("first", 33)} interpretation of the instructions')
    print(f'The end position of the submarine will be: {color_text(pos, 32)}')
    print(f'The product of these values is: {color_text(pos[0] * pos[1], 32)}')

    dirs = {'forward': [0, 1, 1], 'up': [-1, 0, 0], 'down': [1, 0, 0]}
    pos = np.array([0, 0, 0])
    for dir, num in inputs:
        pos += np.array(dirs[dir]) * np.array([num, num, num*pos[0]])

    print(f'\nAccording to the {color_text("second", 33)} interpretation of the instructions')
    print(f'The end position of the submarine will be: {color_text(pos, 32)}')
    print(f'The product of these values is: {color_text(pos[1] * pos[2], 32)}')
