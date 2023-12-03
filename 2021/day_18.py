# Day 18 of Advent of Code 2021
# Snailfish

# We descend into the ocean trench and encounter some snailfish. They say they saw the sleigh keys! They'll even tell
# us which direction the keys went if we help one of the smaller snailfish with their math homework.

# Snailfish numbers aren't like regular numbers. Instead, every snailfish number is a pair - an ordered list of two
# elements. Each element of the pair can be either a regular number or another pair. Pairs are written as [x,y],
# where x and y are the elements within the pair.

# This snailfish's homework is about addition. To add two snailfish numbers, form a pair from the left and right
# parameters of the addition operator. For example, [1,2] + [[3,4],5] becomes [[1,2],[[3,4],5]]

# There's only one problem: snailfish numbers must always be reduced, and the process of adding two snailfish
# numbers can result in snailfish numbers that need to be reduced. To reduce a snailfish number, you must repeatedly
# do the first action in this list that applies to the snailfish number:
#   - If any pair is nested inside four pairs, the leftmost such pair explodes.
#   - If any regular number is 10 or greater, the leftmost such regular number splits.

# To explode a pair, the pair's left value is added to the first regular number to the left of the exploding pair
# (if any), and the pair's right value is added to the first regular number to the right of the exploding pair (if any).
# Exploding pairs will always consist of two regular numbers. Then, the entire exploding pair is replaced with the
# regular number 0.

# To split a regular number, replace it with a pair; the left element of the pair should be the regular number divided
# by two and rounded down, while the right element of the pair should be the regular number divided by two and rounded
# up. For example, 10 becomes [5,5], 11 becomes [5,6], 12 becomes [6,6], and so on.

# To check whether it's the right answer, the snailfish teacher only checks the magnitude of the final sum.
# The magnitude of a pair is 3 times the magnitude of its left element plus 2 times the magnitude of its right element.
# The magnitude of a regular number is just that number.

from itertools import permutations
from math import ceil, floor

from aoc.helpers import *


def first_int(number):
    for i, el in enumerate(number):
        if isinstance(el, int):
            return i, el
    return None


def explode(number, i):
    pair = [number[i + 1], number[i + 3]]
    if left := first_int(number[i::-1]):
        number[i - left[0]] += pair[0]
    if right := first_int(number[i + 4 :]):
        number[i + 4 + right[0]] += pair[1]
    number[i : i + 5] = [0]
    return number


def split(number, i):
    number[i : i + 1] = ["[", floor(number[i] / 2), ",", ceil(number[i] / 2), "]"]
    return number


def reduce(number):
    # First check if there are any pairs that need to be exploded
    depth = 0
    for i, el in enumerate(number):
        if isinstance(el, str):
            if el == "[":
                depth += 1
            elif el == "]":
                depth -= 1
            if depth > 4:
                number = explode(number, i)
                number = reduce(number)
                break

    # After exploding all pairs split numbers that are too large
    for i, el in enumerate(number):
        if isinstance(el, int) and el >= 10:
            number = split(number, i)
            number = reduce(number)
            break

    return number


def add(left, right):
    concat = ["[", *left, ",", *right, "]"] if left else right
    result = reduce(concat)
    # print('  ', ''.join(map(str, left)))
    # print('+ ', ''.join(map(str, right)))
    # print('= ', ''.join(map(str, result)), end='\n\n')
    return result


def calc_mag(number):
    mag = 0
    left, right = number
    left = left if isinstance(left, int) else calc_mag(left)
    right = right if isinstance(right, int) else calc_mag(right)
    mag += 3 * left + 2 * right
    return mag


if __name__ == "__main__":
    numbers = [
        [int(char) if char.isnumeric() else char for char in re.findall(r"(\[|]|,|[0-9]+)", line)]
        for line in import_input("\n", example=False)
    ]

    # Calculate the homework results by adding up all the given snailfish numbers
    result = []
    for number in numbers:
        result = add(result, number)
    result = eval("".join(map(str, result)))

    print("homework result:", result)
    print("homework magnitude:", calc_mag(result))

    # On the back of the homework there is another question:
    # What is the largest magnitude you can get from adding only two of the snailfish numbers?
    max_mag = 0
    for combination in permutations(numbers, 2):
        result = add(combination[0], combination[1])
        result = eval("".join(map(str, result)))
        mag = calc_mag(result)
        max_mag = max(max_mag, mag)

    print("maximum magnitude:", max_mag)
