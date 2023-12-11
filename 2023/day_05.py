# Day 5 of Advent of Code 2023
# If You Give A Seed A Fertilizer

# We take a boat further onto Island Island to find a gardener that is supposed to know
# more about the islands water supply. We find the gardener and point out that Snow island
# is no longer receiving water, they explain that they ran out of sand to filter the water.
# He points us to a ferry that will bring us to the source of the sand. While we wait for
# the ferry the Elf asks us to make sense of the newest edition of the Island Island Almanac.
# It describes what seeds to plant, what fertilizer to use, where to plant the seeds, and so on.
# Our job is to find out what seeds are supposed to be planted in what location for the best yield.

from datetime import timedelta
from timeit import default_timer as timer

from aoc.helpers import *


def get_numbers(line):
    return list(map(int, re.findall(r"\d+", line)))


def get_seed_for_location(location):
    seed = location
    for mapping in mappings:
        for (dst_min, dst_max), (src_min, src_max) in mapping:
            if src_min <= seed <= src_max:
                seed = dst_min + seed - src_min
                break
    return location, seed


def create_mappings(inputs):
    mappings = []
    for i, mapping in enumerate(inputs[::-1]):
        mappings.append([])
        key, *mapping = mapping.split("\n")
        maps = sorted((int(src), int(dst), int(length)) for dst, src, length in map(str.split, mapping))
        for j, (src_min, dst_min, length) in enumerate(maps):
            mappings[i].append(((src_min, src_min + length), (dst_min, dst_min + length)))
    return mappings


if __name__ == "__main__":
    inputs = import_input("\n\n")
    seeds = get_numbers(inputs.pop(0))
    mappings = create_mappings(inputs)

    locations = []
    for seed in seeds:
        locations.append(get_seed_for_location(seed)[0])
    print("The lowest location number:", c(min(locations), Color.GREEN))

    # This might take a couple of minutes XD
    start = timer()
    for loc in range(max([max(dst) for src, dst in mappings[-1]])):
        print(f"\r{timedelta(seconds=(timer() - start))}", end="")
        location, seed = get_seed_for_location(loc)
        if any([seeds[i] <= seed <= seeds[i] + seeds[i + 1] for i in range(0, len(seeds), 2)]):
            print(f"\rseed {seed} -> location: {c(location, Color.GREEN)}")
            break
