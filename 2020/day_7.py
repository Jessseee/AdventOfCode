# Day 7 Advent of Code
# Where to put my shiny golden bag
import re

from aoc.helpers import *

searched_bag = "shiny gold"


def contains(inner_bag):
    count = 0
    containing_bags = [rule[0] for rule in luggage_rules.items() if inner_bag in rule[1]]
    if containing_bags:
        print(inner_bag)
        print(containing_bags)
        for bag in containing_bags:
            count += contains(bag)
    else:
        return count


def contained_in(outer_bag, count=0):
    contained_bags = luggage_rules[outer_bag]
    if not contained_bags:
        return count
    print(outer_bag)
    print(contained_bags)
    print(count)
    for bag in contained_bags:
        if bag != "no other":
            count += int(bag[:1]) * contained_in(bag[2:], count)
    return count


if __name__ == "__main__":
    luggage_rules = re.sub("bags?", "", import_input().read()).replace(".", "").split("\n")
    luggage_rules = [rule.split("contain") for rule in luggage_rules]
    luggage_rules = {rule[0].strip(): [bag.strip() for bag in rule[1].split(",")] for rule in luggage_rules}
    print(luggage_rules)
    print(contained_in(searched_bag))
