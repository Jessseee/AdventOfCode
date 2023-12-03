# Day <DAY> of Advent of Code <YEAR>
# <PUZZLE TITLE>
import re
from dataclasses import dataclass, field
from typing import Dict, List

from aoc.helpers import *


@dataclass
class Node:
    name: str
    weight: int
    children: List["Node"] = field(default_factory=list)
    parent: "Node" = None

    def __repr__(self):
        parent = f"<{self.parent.name}> " if self.parent else ""
        children = f" -> {self.children}" if self.children else ""
        return f"{parent}{self.name}({self.weight}){children}"

    def cumulative_weight(self):
        weight = self.weight
        if self.children:
            weight += sum([child.cumulative_weight() for child in self.children])
        return weight

    def balanced(self):
        if not self.children:
            return True, None
        weights = []
        for child in self.children:
            balanced, correction = child.balanced()
            if balanced:
                weights.append(child.cumulative_weight())
            else:
                return False, correction
        for i in range(len(weights)):
            if weights[i] != weights[0]:
                unbalanced_node = self.children[i]
                return False, (unbalanced_node.name, unbalanced_node.weight - (weights[i] - weights[0]))
        return True, None


class Tree:
    def __init__(self, inputs):
        self.nodes = dict()
        for node in inputs:
            name, weight, _ = node
            self.nodes[name] = Node(name, int(weight))

        for node in inputs:
            parent_name, weight, child_names = node
            if child_names != "":
                for child_name in child_names.split(", "):
                    self.nodes[child_name].parent = self.nodes[parent_name]
                    self.nodes[parent_name].children.append(self.nodes[child_name])

        for node in self.nodes.values():
            if node.parent is None:
                self.base_node = node


if __name__ == "__main__":
    inputs = import_input(example=False).read()
    pattern = re.compile(r"(\w+) \((\d+)\)(?: -> (.+))?")
    inputs = re.findall(pattern, inputs)

    tree = Tree(inputs)
    print(tree.base_node.name)
    print(tree.base_node.balanced())
