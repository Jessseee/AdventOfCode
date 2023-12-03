# Day <DAY> of Advent of Code <YEAR>
# <PUZZLE TITLE>
from collections import Counter

import numpy as np

from aoc.helpers import *

if __name__ == "__main__":
    inputs = np.array(import_input("\n", list, example=True))
    for column in inputs.transpose():
        print(Counter(column).most_common()[0][0], end="\t")
        print(Counter(column).most_common()[-1][0])
