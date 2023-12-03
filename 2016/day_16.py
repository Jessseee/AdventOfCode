# Day <DAY> of Advent of Code <YEAR>
# <PUZZLE TITLE>
import numpy as np

from aoc.helpers import *

if __name__ == "__main__":
    data = input_data = np.array(import_input("", int, example=False), dtype=bool)
    disk_size = 35651584

    while len(data) < disk_size:
        inverse = np.invert(data[::-1])
        data = np.array([*data, False, *inverse])
    data = data[:disk_size]
    print(data.astype(int))

    checksum = data
    while True:
        new_checksum = []
        for i in range(0, len(checksum) - 1, 2):
            new_checksum.append(checksum[i] == checksum[i + 1])
        checksum = new_checksum
        if len(checksum) % 2 != 0:
            break
    print("".join(map(str, np.array(checksum).astype(int))))
