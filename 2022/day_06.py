# Day 6 of Advent of Code 2022
# Tuning Trouble

# As we finally start the expedition on foot, we are given an old and rusty
# communication device. It barely works, but it is still able to receive a
# seemingly-random stream of characters. Our job is to add a subroutine to the
# device to detect start-of-packet and start-of-message markers in the data stream.
# The start-of-packet markers consist of 4 characters that are all different.
# Similarly, the start-of-message marker consists of 14 different characters.
# We need to find out when the first of these markers are send in the incoming
# transmission.

from aoc.helpers import *


def find_marker(signal, marker_len):
    for char in range(marker_len - 1, len(signal)):
        marker = set(signal[char - marker_len : char])
        if len(marker) == marker_len:
            return char, marker


if __name__ == "__main__":
    signals = import_input("\n", example=False)
    for signal in signals:
        chars, marker = find_marker(signal, 4)
        print(f"The start-of-packet marker appears after " f"{c(chars, Color.GREEN)} characters: {marker}")
        chars, marker = find_marker(signal, 14)
        print(f"The start-of-message marker appears after " f"{c(chars, Color.GREEN)} characters: {marker}")
