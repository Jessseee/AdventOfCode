# Day <DAY> of Advent of Code <YEAR>
# <PUZZLE TITLE>
from aoc.helpers import *


def duplicates(items):
    for i in range(len(items)):
        if items[i] in items[i + 1 :]:
            return 0
    return 1


if __name__ == "__main__":
    inputs = import_input("\n", example=False)

    words = [passphrase.split(" ") for passphrase in inputs]
    num_valid = sum(map(duplicates, words))
    print(f"No duplicates rule: {num_valid}/{len(inputs)} passphrases are {c('valid', 32)}.")

    words = [list(map(sorted, passphrase.split(" "))) for passphrase in inputs]
    num_valid = sum(map(duplicates, words))
    print(f"No anagrams rule: {num_valid}/{len(inputs)} passphrases are {c('valid', 32)}.")
