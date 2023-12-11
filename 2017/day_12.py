# Day <DAY> of Advent of Code <YEAR>
# <PUZZLE TITLE>
from dataclasses import field

from aoc.helpers import *


class Network:
    def __init__(self, connections):
        self.nodes = {}
        for connection in connections:
            source, target = connection.split(" <-> ")
            self.nodes[int(source)] = list(map(int, target.split(", ")))

    def find_groups(self):
        nodes = self.nodes.copy()
        groups = []
        while len(nodes.keys()) > 0:
            node = list(nodes.keys())[0]
            group = self.find_group(node)
            groups.append(group)
            nodes = {k: v for k, v in nodes.items() if k not in group}
        return groups

    def find_group(self, id, group=None):
        group = group or []
        for node in self.nodes[id]:
            if node in group:
                continue
            group.append(node)
            self.find_group(node, group)
        return group


if __name__ == "__main__":
    connections = import_input("\n")
    network = Network(connections)
    print(f"There are {c(len(network.find_group(0)), 32)} programs connected to the program with ID 0.")
    print(f"There are {c(len(network.find_groups()), 32)} unconnected groups in the network.")
