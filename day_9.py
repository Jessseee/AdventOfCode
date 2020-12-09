# Day 9 Advent of Code
# cracking the XMAS cypher
from helpers import *
import itertools as itr
preamble_len = 25


def compare_to_preamble(index):
    preamble = sequence[index-preamble_len:index]
    for number, other in itr.combinations(preamble, 2):
        if number+other == sequence[index]:
            return compare_to_preamble(index+1)
    return sequence[index]


def find_weakness(invalid_number):
    for number in sequence:
        contiguous_set = []
        for other in sequence[number:]:
            contiguous_set.append(other)
            if sum(contiguous_set) == invalid_number:
                weakness = min(contiguous_set) + max(contiguous_set)
                return weakness


if __name__ == '__main__':
    sequence = [int(i) for i in import_input().read().split('\n')]
    invalid_nr = compare_to_preamble(preamble_len)
    weak_nr = find_weakness(invalid_nr)
    print(invalid_nr)
    print(weak_nr)

