# Day 9 of Advent of Code 2023
# Mirage Maintenance

# After our adventures Camel ride we find ourselves at an oasis. Looking up we see
# another floating island, completely made of metal. This must be where we can get
# the parts to fix the sand machines. However, before we continue our journey we
# notice the delicate ecosystem of the oasis and decide to take some ecological
# readings. We take out our Oasis And Sand Instability Sensor (OASIS) and produce
# a report of some values changing over time. Our task is to create a model that
# extrapolates the values from these historic readings. This way we can help the
# Elfs predict and prevent any environmental instabilities in the future.


import numpy as np

from aoc.helpers import *


def extrapolate(array):
    diff_table = [array]
    while any(diff_table[-1]):
        diff_table.append(np.diff(diff_table[-1]))
    return sum(diff[-1] for diff in diff_table)


if __name__ == "__main__":
    histories = import_input("\n", parse_integers, example=False)
    print("Sum of extrapolated history data:", sum(extrapolate(history) for history in histories))
    print("Sum of backwards extrapolated history data:", sum(extrapolate(history[::-1]) for history in histories))
