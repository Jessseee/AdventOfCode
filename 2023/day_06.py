# Day 6 of Advent of Code 2023
# Wait For It

# The ferry brings us across Island Island, however there is no large pile of sand
# in sight. We notice a poster that mentions a boat race, with as grand prize an
# all-expenses-paid trip to Desert Island. That must be where the sand comes from.
# We must win this boat race. However, it turns out to be a model boat race, that
# can is won by traversing the longest distance in the set amount of time. The boats
# are powered up by holding a button, the longer we press the button the farther our
# boat will go. However, the time holding the button counts to our total race time.
# Our task is to find the optimal time to hold the button for to break the current
# race records and win the race.

import numpy as np

from aoc.helpers import *


def num_wins(a, b):
    minimum = np.round(1 / 2 * (a - np.sqrt(a * a - 4 * b)))
    maximum = np.round(1 / 2 * (a + np.sqrt(a * a - 4 * b)))
    return int(maximum - minimum)


if __name__ == "__main__":
    races = list(zip(*import_input("\n", parse_integers, example=False)))
    wins = np.prod([num_wins(time, dist) for time, dist in races])
    print("Product of possible number of wins for multiple races:", c(wins, Color.GREEN))

    time, dist = list(import_input("\n", lambda x: int("".join(x.split()[1:])), example=False))
    wins = num_wins(time, dist)
    print("Number of wins for single race:", c(wins, Color.GREEN))
