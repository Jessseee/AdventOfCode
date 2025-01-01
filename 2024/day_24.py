# Day 24 of Advent of Code 2024
# Crossed Wires

import re
import unittest

import operator

from aoc.helpers import import_input, parse_input


def parser(inputs):
    wires, gates = inputs.split("\n\n")
    wires = [wire.split(": ") for wire in wires.split("\n")]
    wires = {key: int(value) for key, value in wires}
    gates = [re.findall(r"[A-Z]+|[a-z0-9]+", gate) for gate in gates.rstrip("\n").split("\n")]
    operators = {"AND": operator.__and__, "OR": operator.__or__, "XOR": operator.__xor__}
    gates = {output: (operators[gate], wire1, wire2) for wire1, gate, wire2, output in gates}
    return wires, gates


def bool_array_to_int(array):
    return sum(bit << idx for idx, bit in enumerate(array))


def int_to_bool_array(number):
    return list(map(int, f"{number:b}"[::-1]))


@parse_input(parser)
def part1(inputs):
    inputs, gates = inputs

    def get_value(wire):
        if (value := inputs.get(wire)) is not None:
            return value
        opr, input1, input2 = gates[wire]
        value1 = get_value(input1)
        value2 = get_value(input2)
        return int(opr(value1, value2))

    return bool_array_to_int([get_value(wire) for wire in sorted(key for key in gates if key.startswith("z"))])


@parse_input(parser)
def part2(inputs):
    wires, gates = inputs
    swapped_wires = set()
    for output, (opr, input1, input2) in gates.items():
        if output.startswith("z") and output != "z45":
            if opr != operator.__xor__:
                swapped_wires.add(output)
        elif (input1.startswith("x") and input2.startswith("y")) or (input1.startswith("y") and input2.startswith("x")):
            if opr == operator.__or__:
                swapped_wires.add(output)
        elif opr == operator.__xor__:
            swapped_wires.add(output)
        elif opr == operator.__or__:
            if gates[input1][0] != operator.__and__:
                swapped_wires.add(input1)
            elif gates[input2][0] != operator.__and__:
                swapped_wires.add(input2)
        elif opr == operator.__or__:
            if gates[input1][0] != operator.__and__:
                swapped_wires.add(input1)
            elif gates[input2][0] != operator.__and__:
                swapped_wires.add(input2)
        elif opr == operator.__and__:
            if gates[input1][0] != operator.__xor__ and gates[input2][0] == operator.__or__:
                swapped_wires.add(input1)
            elif gates[input1][0] == operator.__or__ and gates[input2][0] != operator.__xor__:
                swapped_wires.add(input2)
    return ",".join(sorted(swapped_wires))


class Tests202424(unittest.TestCase):
    def test_part1(self):
        inputs = (
            "x00: 1\n"
            "x01: 0\n"
            "x02: 1\n"
            "x03: 1\n"
            "x04: 0\n"
            "y00: 1\n"
            "y01: 1\n"
            "y02: 1\n"
            "y03: 1\n"
            "y04: 1\n"
            "\n"
            "ntg XOR fgs -> mjb\n"
            "y02 OR x01 -> tnw\n"
            "kwq OR kpj -> z05\n"
            "x00 OR x03 -> fst\n"
            "tgd XOR rvg -> z01\n"
            "vdt OR tnw -> bfw\n"
            "bfw AND frj -> z10\n"
            "ffh OR nrd -> bqk\n"
            "y00 AND y03 -> djm\n"
            "y03 OR y00 -> psh\n"
            "bqk OR frj -> z08\n"
            "tnw OR fst -> frj\n"
            "gnj AND tgd -> z11\n"
            "bfw XOR mjb -> z00\n"
            "x03 OR x00 -> vdt\n"
            "gnj AND wpb -> z02\n"
            "x04 AND y00 -> kjc\n"
            "djm OR pbm -> qhw\n"
            "nrd AND vdt -> hwm\n"
            "kjc AND fst -> rvg\n"
            "y04 OR y02 -> fgs\n"
            "y01 AND x02 -> pbm\n"
            "ntg OR kjc -> kwq\n"
            "psh XOR fgs -> tgd\n"
            "qhw XOR tgd -> z09\n"
            "pbm OR djm -> kpj\n"
            "x03 XOR y03 -> ffh\n"
            "x00 XOR y04 -> ntg\n"
            "bfw OR bqk -> z06\n"
            "nrd XOR fgs -> wpb\n"
            "frj XOR qhw -> z04\n"
            "bqk OR frj -> z07\n"
            "y03 OR x01 -> nrd\n"
            "hwm AND bqk -> z03\n"
            "tgd XOR rvg -> z12\n"
            "tnw OR pbm -> gnj"
        )
        expected = 2024
        self.assertEqual(expected, part1(inputs))


if __name__ == "__main__":
    inputs = import_input()
    print("part 1:", part1(inputs))
    print("part 2:", part2(inputs))
