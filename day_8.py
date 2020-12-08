# Day 8 Advent of Code
# GameBoy troubles
import operator
from helpers import *

ops = {
    '+': operator.add,
    '-': operator.sub
}


def apply_operation(oprnd_1, opr, oprnd_2):
    """
    :param oprnd_1: The first operand
    :param opr: The operator
    :param oprnd_2: The second operand
    :return: The result of the operation
    """
    return ops.get(opr)(int(oprnd_1), int(oprnd_2))


def rewrite_instruction(index, instruction, new_instruction, acc, visited):
    """
    :param index: The instruction to be rewritten
    :param instruction: The list of instructions
    :param new_instruction: The instruction to rewrite to
    :param acc: The current accumulator value
    :param visited: The current list of visited instructions
    :return: The rewritten instruction to be executed
    """
    print(color_text(f'\t{instruction[0]} -> {new_instruction}', 31))
    instructions[index] = f'{new_instruction} {instruction[1]}'
    return execute_instruction(index, acc, visited[:-1], True)


def execute_instruction(index=0, acc=0, visited=[], changed=False):
    """
    :param index: The current instruction's index
    :param acc: The current accumulator value
    :param visited: The current list of visited instructions
    :param changed: If a instruction has been rewritten
    :return: The next instruction to be executed or if the instructions have been terminated
    """
    # If instruction is empty the program has terminated successfully
    if not instructions[index]:
        print(color_text("Terminated successfully!", 32))
        return True

    # If instruction is already visited it will end in an infinite loop
    if index not in visited:
        visited.append(index)
    else:
        print(color_text("\tInfinite loop!\n", 31))
        return False

    instruction = instructions[index].split(' ')
    opr, val = instruction[1][:1], instruction[1][1:]

    if changed:
        print(color_text(f'\t{index}:   \t{instruction}   \t{acc}', 37))
    else:
        print(color_text(f'{index}:   \t{instruction}   \t{acc}', 38))

    if instruction[0] == 'acc':
        return execute_instruction(
            index + 1,
            apply_operation(acc, opr, val),
            visited,
            changed
        )
    elif instruction[0] == 'nop':
        if not changed and rewrite_instruction(index, instruction, 'jmp', acc, visited):
            return
        return execute_instruction(
            index + 1,
            acc,
            visited,
            changed
        )
    elif instruction[0] == 'jmp':
        if not changed and rewrite_instruction(index, instruction, 'nop', acc, visited):
            return
        return execute_instruction(
            apply_operation(index, opr, val),
            acc,
            visited,
            changed
        )


if __name__ == '__main__':
    instructions = import_input().read().split('\n')
    execute_instruction()
