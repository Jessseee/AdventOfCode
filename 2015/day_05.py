# Day 6 of Advent of Code 2015
# Doesn't He Have Intern-Elves For This?
import re

from aoc.helpers import *

rules = [
    re.compile(r"^(?!.*(ab|cd|pq|xy)).*$"),
    re.compile(r"^(.*[aeiou].*[aeiou].*[aeiou].*)$"),
    re.compile(r"^.*(.)\1.*$"),
]

new_rules = [re.compile(r"^.*(..).*\1.*$"), re.compile(r"^.*(.).\1.*$")]


if __name__ == "__main__":
    inputs = import_input("\n", example=False)
    nice_strings = [line for line in inputs if all([bool(rule.match(line)) for rule in rules])]
    new_nice_strings = [line for line in inputs if all([bool(rule.match(line)) for rule in new_rules])]
    for line in inputs:
        print(line)
        print([bool(rule.match(line)) for rule in new_rules])
    print(len(new_nice_strings))
