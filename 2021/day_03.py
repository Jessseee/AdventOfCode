# Day 3 of Advent of Code 2021
# Binary Diagnostic
from helpers import *
from collections import Counter


def find_power_consumption(inputs):
    counter = [[0, 0] for _ in range(12)]
    for line in inputs:
        for i, bit in enumerate(line):
            counter[i][int(bit)] += 1
    gamma = ''
    epsilon = ''
    for bits in counter:
        gamma += str(bits.index(max(bits)))
        epsilon += str(bits.index(min(bits)))
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return gamma * epsilon


def find_rating(inputs, crit):
    i = 0
    while len(inputs) > 1:
        bits = Counter([line[i] for line in inputs])
        if bits['0'] == bits['1']:
            bit = (['1', '0'][crit])
        else:
            bit = bits.most_common()[crit][0]
        inputs = [line for line in inputs if line[i] == bit]
        i += 1
    return inputs[0]


if __name__ == '__main__':
    inputs = import_input('\n')
    print(find_power_consumption(inputs))
    print(int(find_rating(inputs, 0), 2) * int(find_rating(inputs, -1), 2))
