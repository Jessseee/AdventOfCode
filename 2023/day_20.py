# Day 20 of Advent of Code 2023
# <PUZZLE TITLE>
import math
from copy import deepcopy
from dataclasses import dataclass, field
from functools import cache

import networkx as nx

from aoc.helpers import *

# <PUZZLE DESCRIPTION>





LOW, HIGH = False, True


@dataclass
class Module:
    name: str
    outputs: list[str] = field(default_factory=list)
    inputs: list[str] = field(default_factory=list)

    def __call__(self, input, pulse):
        raise NotImplementedError

    def propagate(self, pulse):
        return [(self.name, module, pulse) for module in self.outputs]


class FlipFlop(Module):
    state: bool = LOW

    def __call__(self, input, pulse):
        if pulse == LOW:
            self.state = not self.state
            return self.propagate(self.state)
        return []


class Conjunction(Module):
    state: dict = None

    def __call__(self, input, pulse):
        if self.state is None:
            self.state = {name: LOW for name in self.inputs}
        self.state[input] = pulse
        return self.propagate(LOW if all(self.state.values()) else HIGH)


class Broadcaster(Module):
    state: bool = LOW

    def __call__(self, input, pulse):
        return self.propagate(pulse)


class Output(Module):
    state: bool = None

    def __call__(self, input, pulse):
        self.state = pulse
        return []


def parse_module(line):
    module, outputs = line.split(" -> ")
    if module == "broadcaster":
        module = "=" + module
    type, name, outputs = module[0], module[1:], outputs.split(", ")
    match type[0]:
        case "%":
            return name, FlipFlop(name, outputs)
        case "&":
            return name, Conjunction(name, outputs)
        case "=":
            return name, Broadcaster(name, outputs)


def link_modules(modules, graph):
    outputs = []
    for module in modules.values():
        graph.add_node(module.name)
        for out_module in module.outputs:
            if out_module in modules:
                modules[out_module].inputs.append(module.name)
                graph.add_edge(module.name, out_module)
            else:
                outputs.append((module, out_module))
        for in_module in module.inputs:
            graph.add_edge(in_module, module.name)
    for module, out_module in outputs:
        modules[out_module] = Output(out_module)
        graph.add_node(out_module)
        graph.add_edge(module.name, out_module)
    return modules


def press_button(modules, cycles):
    accumulated_pulses = [0, 0]
    sent_pulses = [("button", "broadcaster", LOW)]

    while len(sent_pulses) > 0:
        in_module, cur_module, pulse = sent_pulses.pop(0)
        # print(in_module, f"—{['LOW', 'HIGH'][pulse]}->", cur_module)
        accumulated_pulses[pulse] += 1
        if cur_module in modules:
            out_modules = modules[cur_module](in_module, pulse)
            sent_pulses += out_modules
        if cur_module == "hb":
            for module, state in modules["hb"].state.items():
                if state and not cycles.get(module, False):
                    cycles[module] = presses
    return accumulated_pulses, cycles


if __name__ == "__main__":
    modules = {k: v for k, v in import_input("\n", parse_module, example=False)}
    graph = nx.DiGraph()
    modules = link_modules(modules, graph)
    nx.draw(
        graph,
        with_labels=True,
        width=1,
        alpha=0.9,
        font_weight="bold",
        arrows=True,
        node_size=[1000 if node == "rx" else 300 for node in graph.nodes],
        node_color=["#85342c" if node == "rx" else "#1f78b4" for node in graph.nodes],
    )
    plt.show()

    total_low = total_high = 0
    presses = 1
    cycles = {}
    while True:
        _, cycles = press_button(modules, cycles)
        presses += 1
        if len(cycles) == 4:
            print(cycles)
            print(math.lcm(*cycles.values()))
            break
