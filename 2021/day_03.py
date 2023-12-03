# Day 3 of Advent of Code 2021
# Binary Diagnostic

# The submarine has been making some odd creaking noises, so we ask it to produce a diagnostic report just in case.
# The diagnostic report consists of a list of binary numbers which, when decoded properly, can tell you many useful
# things about the conditions of the submarine.

from collections import Counter

from aoc.helpers import *


def find_power_consumption(inputs):
    """
    :param list inputs: The original input
    :return: The calculated power consumption
    """
    counter = [[0, 0] for _ in range(12)]
    for line in inputs:
        for i, bit in enumerate(line):
            counter[i][int(bit)] += 1
    gamma = ""
    epsilon = ""
    for bits in counter:
        gamma += str(bits.index(max(bits)))
        epsilon += str(bits.index(min(bits)))
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return gamma * epsilon


def find_rating(inputs: list, crit: int) -> int:
    """
    :param list inputs: The original input
    :param int crit: Should get min/max value
    :return: The calculated rating
    """
    i = 0
    while len(inputs) > 1:
        bits = Counter([line[i] for line in inputs])
        if bits["0"] == bits["1"]:
            bit = ["1", "0"][crit]
        else:
            bit = bits.most_common()[crit][0]
        inputs = [line for line in inputs if line[i] == bit]
        i += 1
    return int(inputs[0], 2)


if __name__ == "__main__":
    inputs = import_input("\n")

    # The first parameter to check is the power consumption.
    # We need to use the binary numbers in the diagnostic report to generate two new binary numbers
    # (gamma & epsilon) The power consumption can then be found by multiplying the these two rates.

    # Each bit in the gamma rate can be determined by finding the most common
    # bit in the corresponding position of all numbers in the diagnostic report.
    print(f"The power consumption: {c('{:,}'.format(find_power_consumption(inputs)), 32)}")

    # Next, we should verify the life support rating, which can be determined by
    # multiplying the oxygen generator rating by the CO2 scrubber rating.

    # We start with the full list of binary numbers and consider just the first bit
    # and select bits by the bit criteria of each rating.

    # For the oxygen generator rating we keep the most common value in the current bit
    # position and for the C02 scrubber rating we keep the least common value.

    # Finally, we take the product of the ratings to get the life support rating.
    oxygen_rating = find_rating(inputs, 0)
    c02_rating = find_rating(inputs, -1)
    print(f"The life support rating: {c('{:,}'.format(oxygen_rating * c02_rating), 32)}")
