# Day 8 of Advent of Code 2021
# Seven Segment Search

# As our submarine slowly makes its way through the cave system, we notice that the four-digit seven-segment
# displays in our submarine are malfunctioning; they must have been damaged during the escape. We'll be in a lot
# of trouble without them, so we better figure out what's wrong.


# Each digit of a seven-segment display is rendered by turning
# on or off any of seven segments named a through g:

#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....
#
#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

# The problem is that the signals which control the segments have been mixed up on each display.
# The submarine is still trying to display numbers by producing output on signal wires a through g,
# but those wires are connected to segments randomly. Worse, the wire/segment connections are mixed
# up separately for each four-digit display!

# For each display, we watch the changing signals for a while, make a note of all ten unique signal
# patterns we see, and then write down a single four digit output value. So, Each entry consists of ten unique
# signal patterns, a | delimiter, and finally the four digit output value.

from aoc.helpers import *


def count_unique_length_digits(inputs):
    return sum([sum([len(digit) in (2, 4, 3, 7) for digit in output]) for _, output in inputs])


def decode_output(inputs, rules):
    total = 0
    for unique, output in inputs:
        known_digits = [set()] * 10
        i = 0
        while not all(known_digits):
            digit = unique[i]
            for key, rule in rules.items():
                if rule(set(digit), known_digits):
                    known_digits[key] = set(digit)
                    break
            i = (i + 1) % len(unique)
        total += int("".join([str(known_digits.index(set(digit))) for digit in output]))
    return total


if __name__ == "__main__":
    inputs = [[el.split(" ") for el in line.split(" | ")] for line in import_input("\n")]

    # First, because the digits 1, 4, 7, and 8 each use a unique number of segments,
    # we should be able to tell which combinations of signals correspond to those digits.
    # So, in the output values, we count how many times digits 1, 4, 7, or 8 appear.
    print(f"The sum of digits with an unique length is: {c(count_unique_length_digits(inputs), 32)}")

    # Through a little deduction, we should now be able to determine the remaining digits.
    rules = {
        1: lambda d, k: len(d) == 2,
        4: lambda d, k: len(d) == 4,
        7: lambda d, k: len(d) == 3,
        8: lambda d, k: len(d) == 7,
        6: lambda d, k: len(d) == 6 and not k[1] <= d,
        0: lambda d, k: len(d) == 6 and not k[4] <= d,
        9: lambda d, k: len(d) == 6,
        3: lambda d, k: len(d) == 5 and k[1] <= d,
        5: lambda d, k: len(d) == 5 and d <= k[6],
        2: lambda d, k: len(d) == 5,
    }

    # With the above rules we can find out each digit in the unique part of the entries and decode the output.
    print(f"The sum of all decoded outputs is: {c('{:,}'.format(decode_output(inputs, rules)), 32)}")
