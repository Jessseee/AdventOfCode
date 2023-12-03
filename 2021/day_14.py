# Day 14 of Advent of Code 2021
# Extended Polymerization

# The incredible pressures at this depth are starting to put a strain on our submarine. The submarine has
# polymerization equipment that would produce suitable materials to reinforce the submarine

# The submarine manual contains instructions for finding the optimal polymer formula; specifically, it offers a polymer
# template and a list of pair insertion rules. We just need to work out what polymer would result after repeating
# the pair insertion process a few times.

# The first line is the polymer template this is the starting point of the process. The following section defines
# the pair insertion rules. A rule like AB -> C means that when elements A and B are immediately adjacent, element C
# should be inserted between them. These insertions all happen simultaneously. We not that pairs overlap: the second
# element of one pair is the first element of the next pair. Also, because all pairs are considered simultaneously,
# inserted elements are not considered to be part of a pair until the next step.

# It is not very efficient to simulate the individual insertions, instead we keep track of the pairs and add pairs
# according to the pair insertion rules. So AB -> C would result in the pairs AC and CB and the AB pair is discarded
# To measure our results we keep track of the quantity of the most common element and subtract the quantity of the
# least common element in the resulting polymer.

from collections import defaultdict

from aoc.helpers import *


def print_results(counter, step):
    sorted_counter = sorted(counter.values())
    print(
        f"After step {str(step+1).zfill(2)}: most common - least common =",
        c("{:,}".format(sorted_counter[-1] - sorted_counter[0]), 32),
    )


if __name__ == "__main__":
    template, insert_pair = import_input("\n\n", example=False)
    template = list(template)
    insert_pairs = {k: v for k, v in [pair.split(" -> ") for pair in insert_pair.split("\n")]}

    pairs = defaultdict(int)
    for i in range(1, len(template)):
        pairs[template[i - 1] + template[i]] += 1

    counter = defaultdict(int)
    for char in template:
        counter[char] += 1

    for step in range(40):
        new_pairs = pairs.copy()
        for pair, count in pairs.items():
            new_pairs[pair] -= count
            insert = insert_pairs[pair]
            new_pairs[pair[0] + insert] += count
            new_pairs[insert + pair[1]] += count
            counter[insert] += count
        pairs = new_pairs
        print_results(counter, step)
