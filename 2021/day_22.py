# Day 22 of Advent of Code 2021
# Reactor Reboot
from itertools import product

from aoc.helpers import *


def inside(ranges1, ranges2):
    return all([r1[0] >= r2[0] and r1[1] <= r2[1] for (r1, r2) in product(ranges1, ranges2)])


def intersect(ranges1, ranges2):
    if any([r2[0] <= r1[0] <= r2[1] or r2[0] <= r1[1] <= r2[1] for (r1, r2) in product(ranges1, ranges2)]):
        return tuple((max(ranges1[i][0], ranges2[i][0]), min(ranges1[i][1], ranges2[i][1])) for i in range(3))
    return False


def volume(ranges):
    x, y, z = ranges
    return (x[1] - x[0] + 1) * (y[1] - y[0] + 1) * (z[1] - z[0] + 1)


def reboot_reactor(instructions, limit):
    reactor = {}
    steps = len(instructions)
    print("limit:", limit)
    for step, line in enumerate(instructions):
        print(f"step {step}/{steps}: {line}")
        state, ranges = line.split(" ")
        is_on = state == "on"
        ranges = tuple((int(r[0]), int(r[1])) for r in re.findall(r"(-?[0-9]+)..(-?[0-9]+)", ranges))
        if limit and not inside(ranges, limit):
            print("outside limit:", ranges, end="\n\n")
            continue
        intersections = {}
        for other_range, other_volume in reactor.items():
            if not (is_on or other_volume > 0):
                continue
            elif intersection := intersect(other_range, ranges):
                if all([not inside(intersection, other_intersection) for other_intersection in intersections.keys()]):
                    print(intersection)
                    intersections[intersection] = volume(intersection) * [-1, 1][is_on and other_volume < 0]
        reactor.update(intersections)
        if is_on:
            reactor[ranges] = volume(ranges)
        print("reactor:", reactor.values(), sum(reactor.values()), end="\n\n")


if __name__ == "__main__":
    instructions = import_input("\n")
    limit = [(-50, 50)] * 3
    reboot_reactor(instructions, limit)
    # reboot_reactor(instructions, None)
