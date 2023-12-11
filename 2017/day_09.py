# Day <DAY> of Advent of Code <YEAR>
# <PUZZLE TITLE>
from enum import Enum

from aoc.helpers import *


class Stream:
    class CharType(int, Enum):
        GROUP = 35
        GARBAGE = 33
        PLAIN = 37
        IGNORED = 31
        OTHER = 29

    def __init__(self, stream):
        self.stream = stream
        self.group_count = 0
        self.garbage_count = 0
        self.cur_group_depth = 0
        self.garbage = False
        self.ignore = False

    def read(self):
        for char in self.stream:
            char_type = self.eval_char(char)
            print(c(char, char_type), end="")

        print(
            f"\nThe stream contains {c(self.group_count, 32)} groups "
            f"and {c(self.garbage_count, 31)} garbage characters.\n"
        )

    def eval_char(self, char):
        if self.ignore:
            self.ignore = False
            return self.CharType.IGNORED
        if char == "!":
            self.ignore = True
            return self.CharType.IGNORED
        if char == ">":
            self.garbage = False
            return self.CharType.GARBAGE
        if self.garbage:
            self.garbage_count += 1
            return self.CharType.PLAIN
        if char == "<":
            self.garbage = True
            return self.CharType.GARBAGE
        if char == "}":
            self.group_count += self.cur_group_depth
            self.cur_group_depth -= 1
            return self.CharType.GROUP
        if char == "{":
            self.cur_group_depth += 1
            return self.CharType.GROUP
        return self.CharType.OTHER


if __name__ == "__main__":
    streams = import_input("\n")
    for stream in streams:
        Stream(stream).read()
