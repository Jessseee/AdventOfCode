# Day 12 of Advent of Code 2023
# Hot Springs

# We reach what seems to be the Hot Springs, only to be corrected by a researcher
# who points out that it's actually an onsen. The real "hot springs" are next door.
# Where we see a small building surrounded by towering metal helixes. Due to a shortage
# of lava on Gear Island, the hot springs aren't functioning properly. The administrative
# staff informs us that the entire Gear Island is offline, and they request our help
# in investigating why the lava has stopped flowing. To get up there we can use one of
# the hot springs. However, the records detailing the condition of each spring are damaged.
# Our task is to identify which springs are safe to use and which are damaged.


from functools import cache

from aoc.helpers import *


def parse_input(row, expanded=False):
    springs, groups = row.split(" ")
    if expanded:
        springs = "?".join([springs] * 5)
        groups = ",".join([groups] * 5)
    return springs + ".", tuple(parse_integers(groups))


@cache
def count(damage, valid):
    if len(valid) == 0:
        return 0 if "#" in damage else 1
    cur, valid = valid[0], valid[1:]
    result = 0
    for i in range(len(damage) - (len(valid) + sum(valid)) - cur):
        if damage[i + cur] == "#":
            continue
        if "#" in damage[:i]:
            break
        if "." not in damage[i : i + cur]:
            result += count(damage[i + cur + 1 :], valid)
    return result


def possible_arrangements(records):
    total = 0
    for springs, valid in records:
        res = count(springs, valid)
        total += res
    return total


if __name__ == "__main__":
    data = import_input("\n")
    records = [parse_input(line) for line in data]
    print("Sum of possible arrangements:", c(possible_arrangements(records), Color.GREEN))
    expanded_records = [parse_input(line, True) for line in data]
    print("Sum of possible arrangements (expanded records):", c(possible_arrangements(expanded_records), Color.GREEN))
