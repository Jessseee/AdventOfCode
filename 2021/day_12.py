# Day 12 of Advent of Code 2021
# Passage Pathing

# With our submarine's subterranean subsystems subsisting suboptimally, the only way we're getting out of this
# cave anytime soon is by finding a path yourself. Not just any path - the only way to know if we've found the best
# path is to find all of them! Fortunately, the sensors are still mostly working, and so you build a rough map
# of the remaining caves.

# The map is in the format `start-A` or `A-c` indicating the connections between caverns. There are two types of caves:
# big caves (written in uppercase, like A) and small caves (written in lowercase, like b).

from collections import Counter

from aoc.helpers import *


def find_path(cave, visited, all_paths, visit_one_twice):
    visited.append(cave)

    # Return all visited paths on reaching the 'end' cave
    if cave == "end":
        all_paths.append(visited)
        return all_paths

    # For each connection of the current cave continue searching
    for connection in all_caves[cave]:
        # Check if the connected cave is allowed to be visited (again)
        can_visit_twice = (
            visit_one_twice
            and not any([v > 1 for k, v in Counter(visited).items() if k.islower()])
            and connection != "start"
            or connection.isupper()
        )
        if connection not in visited or can_visit_twice:
            all_paths = find_path(connection, visited.copy(), all_paths, visit_one_twice)

    # After searching through all the connected caves return the visited paths
    return all_paths


if __name__ == "__main__":
    all_caves = {}

    # Let's create a (reverse) mapping of all the connected caves
    for con in import_input("\n", example=False):
        cave, connected = con.split("-")
        if not all_caves.get(cave):
            all_caves[cave] = [connected]
        else:
            all_caves[cave].append(connected)
        if not all_caves.get(connected):
            all_caves[connected] = [cave]
        else:
            all_caves[connected].append(cave)

    # First our goal is to find the number of distinct paths that start at start, end at end, and don't visit
    # small caves more than once as it would be a waste of time to. But big caves are large enough that it might
    # be worth visiting them multiple times.
    print(
        f"There are {c(len(find_path('start', [], [], False)), 32)} distinct paths when only visiting small caves once."
    )

    # After reviewing the available paths, we realized we might have time to visit a single small cave twice.
    # Specifically, big caves can be visited any number of times, a single small cave can be visited at most twice,
    # and the remaining small caves can be visited at most once. But, we should never visit cave 'start' or 'end' twice.
    print(
        f"There are {c(len(find_path('start', [], [], True)), 32)} distinct paths when visiting one small cave twice."
    )
