# Day 7 of Advent of Code 2022
# No Space Left On Device

# The device we received from the Elves needs an update. However, there seems to b eno space left on
# it's hard drive. We browse around the file-system and log the terminal output. Our job is to calculate
# the sizes of the nested directories and find a suitable directory to remove to create enough space
# for the update.

from collections import defaultdict

from aoc.helpers import *


class Directory(defaultdict):
    def __init__(self, name="dir", size=0):
        super().__init__(Directory)
        self.name = name
        self.size = size

    def __repr__(self):
        return f"{self.name} (dir, size={self.size})"

    def print_content(self, directory=None, depth=0, result=""):
        directory = directory or self
        for key, item in directory.items():
            offset = c(depth * " | ", Color.GREY)
            if not isinstance(item, defaultdict):
                print(f"{offset} {key} (file, size={item})")
            else:
                print(f"{offset} {key} (dir, size={directory.size})")
                self.print_content(item, depth + 1, result)

    def resolve_subdir_size(self, directory=None):
        directory = directory or self
        size = 0
        for key, item in directory.items():
            if isinstance(item, defaultdict):
                size += self.resolve_subdir_size(item)
            else:
                size += item
        directory.size = size
        return size

    def get_subdirs_by_condition(self, condition, directory=None, result=None):
        directory = directory or self
        if result is None:
            result = []
        if condition(directory):
            result.append(directory)
        for key, item in directory.items():
            if isinstance(item, defaultdict):
                result = self.get_subdirs_by_condition(condition, item, result)
        return result

    def __radd__(self, other):
        return other + self.size

    def __lt__(self, other):
        return self.size < other.size

    def __gt__(self, other):
        return self.size > other.size

    def __eq__(self, other):
        return self.size == other.size


def resolve_tree(inputs):
    depth = []
    current_directory = root_directory = Directory("/")
    for line in inputs:
        line = line.split(" ")
        if line[:2] == ["$", "cd"]:
            directory = line[2]
            if directory == "..":
                depth.pop()
            else:
                depth.append(directory)
            current_directory = root_directory
            for directory in depth:
                current_directory = current_directory[directory]
                current_directory.name = directory
        elif line[:2] == ["$", "ls"]:
            pass
        else:
            size, item_name = line
            if size == "dir":
                current_directory[item_name] = Directory(item_name)
            else:
                current_directory[item_name] = int(size)
    return root_directory


if __name__ == "__main__":
    inputs = import_input("\n", example=False)

    root_directory = resolve_tree(inputs)
    root_directory.resolve_subdir_size()
    root_directory.print_content()
    print()

    def condition(directory):
        return directory.size <= 100000

    directories_at_most_100000 = sum(root_directory.get_subdirs_by_condition(condition))
    print(
        f"the cumulative size of directories with a size of at most 100K: "
        f"{c(directories_at_most_100000, Color.GREEN)}"
    )

    required_space, free_space = 30000000, (70000000 - root_directory.size)

    def condition(directory):
        return directory.size >= required_space - free_space

    directory_to_delete = min(root_directory.get_subdirs_by_condition(condition))
    print(f"The smallest directory to delete to create space for the update: " f"{c(directory_to_delete, Color.GREEN)}")
