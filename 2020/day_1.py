# Day 1 of Advent of Code
# Fix your expense report
import itertools as itr

import numpy as np

file_name = "input/input_day_1.txt"


def find_sum_with_result(nr, result):
    """
    :param nr: number of items that should sum to result
    :param result: The result of the sum of items we are looking for
    :return: The product of a set of items that sum up to the given result.
    """
    with open(file_name) as f:
        lines = f.readlines()
        integers = [int(i) for i in lines]
        for items in itr.combinations(integers, nr):
            if sum(items) == result:
                return f"{items}\n" f"sum = {result}\n" f"product = {np.prod(np.array(items))}\n"


if __name__ == "__main__":
    print(find_sum_with_result(2, 2020))
    print(find_sum_with_result(3, 2020))
