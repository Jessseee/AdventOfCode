# Day <DAY> of Advent of Code <YEAR>
# <PUZZLE TITLE>
from helpers import *
import numpy as np
from collections import Counter


if __name__ == '__main__':
    inputs = np.array(import_input('\n', list, example=True))
    for column in inputs.transpose():
        print(Counter(column).most_common()[0][0], end='\t')
        print(Counter(column).most_common()[-1][0])
