# Day 8 of Advent of Code 2021
# Seven Segment Search
from helpers import *

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
    2: lambda d, k: len(d) == 5
}


def count_unique_length_digits(inputs):
    return sum([sum([len(digit) in (2, 4, 3, 7) for digit in output]) for _, output in inputs])


def decode_output(inputs):
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
            i = (i+1) % len(unique)
        total += int(''.join([str(known_digits.index(set(digit))) for digit in output]))
    return total


if __name__ == '__main__':
    inputs = [[el.split(' ') for el in line.split(' | ')] for line in import_input('\n')]

    print(f'The sum of digits with an unique length is: {color_text(count_unique_length_digits(inputs), 32)}')
    print(f"The sum of all decoded outputs is: {color_text('{:,}'.format(decode_output(inputs)), 32)}")


