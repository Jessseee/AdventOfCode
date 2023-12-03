# Day <DAY> of Advent of Code <YEAR>
# <PUZZLE TITLE>
import hashlib
from copy import copy

from aoc.helpers import *


def create_hash(value, stretch):
    result = copy(value)
    for _ in range(stretch + 1):
        result = hashlib.md5(result.encode("utf-8")).hexdigest()
    return result


if __name__ == "__main__":
    salt = import_input(example=False).read()
    hashes = []
    keys = []
    stretch = 2016
    i = 0
    while len(keys) < 64:
        if i >= len(hashes):
            hashes.append(create_hash(salt + str(i), stretch))
        # Match *exactly* 3 of the same character
        if match := re.search(r"(.)\1\1", hashes[i]):
            j = 1
            while j <= 1000:
                if i + j >= len(hashes):
                    hashes.append(create_hash(salt + str(i + j), stretch))
                # Match *exactly* 5 of the same character
                if re.search(rf"({match.group(1)})\1\1\1\1", hashes[i + j]):
                    keys.append(hashes[i])
                    print("\n", len(keys), "\t", i, hashes[i], match.group(1))
                    print("\t\t", i + j, hashes[i + j])
                    break
                j += 1
        i += 1
