# Day <DAY> of Advent of Code <YEAR>
# <PUZZLE TITLE>
from helpers import *
import re
import numpy as np


def count_correct_triangles(triangles):
    correct_triangles = 0
    for triangle in triangles:
        triangle = sorted(triangle)
        correct_triangles += triangle[0] + triangle[1] > triangle[2]
    print(correct_triangles)


if __name__ == '__main__':
    inputs = np.array(import_input('\n', lambda line: list(map(int, re.findall(r'\d+', line))), example=False))
    count_correct_triangles(inputs)

    inputs = inputs.transpose().flatten()
    inputs = [inputs[i:i+3] for i in range(0, len(inputs), 3)]
    count_correct_triangles(inputs)

