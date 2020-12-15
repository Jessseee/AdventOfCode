# Day 14 Advent of Code
# Fixing the sea port computer
from helpers import *


def apply_bitmask_v1(value, bitmask):
    bin_value = format(value, f'0{MASK_LEN}b')
    for i in range(MASK_LEN):
        if bitmask[i] == 'X':
            continue
        else:
            replace_chr(i, bitmask[i], bin_value)
    return int(bin_value, 2)


def run_init_program_v1(instructions):
    mem = [0] * max([int(value) for key, value in instructions if key[:3] == 'mem'])
    cur_mask = 'X' * MASK_LEN
    for instruction, value in instructions:
        if instruction == 'mask':
            print(f'changed mask to [{value}]')
            cur_mask = value
        elif instruction[:3] == 'mem':
            masked_value = apply_bitmask_v1(int(value), cur_mask)
            mem_adr = int(instruction[4:-1])
            mem[mem_adr] = masked_value
            print(f'mem[{mem_adr}] = {masked_value}')
    return mem


def apply_bitmask_v2(address, bitmask):
    bin_adr = format(address, f'0{MASK_LEN}b')
    floating = []
    addresses = []
    for i in range(MASK_LEN):
        if bitmask[i] == '0':
            continue
        if bitmask[i] == '1':
            bin_adr = replace_chr(i, '1', bin_adr)
        if bitmask[i] == 'X':
            floating.append(i)
    for i in range(2**len(floating)):
        address = bin_adr
        for index in floating:
            address = replace_chr(index, str(i % 2), address)
            i = i//2
        addresses.append(int(address, 2))
    return addresses


def run_init_program_v2(instructions):
    mem = dict()
    cur_mask = '0' * 36
    for instruction, value in instructions:
        if instruction == 'mask':
            print(f'changed mask to [{value}]')
            cur_mask = value
        elif instruction[:3] == 'mem':
            mem_adrs = apply_bitmask_v2(int(instruction[4:-1]), cur_mask)
            for mem_adr in mem_adrs:
                mem[mem_adr] = int(value)
                print(f'mem[{mem_adr}] = {value}')
    return mem.values()


if __name__ == '__main__':
    input = import_input().read().split('\n')
    instructions = [[key, value] for key, value in [key_value.split(' = ') for key_value in input]]
    MASK_LEN = 36
    print(f'(V1 decoder chip sim)\nSum of memory values: {sum(run_init_program_v1(instructions))}')
    print(f'(V2 decoder chip sim)\nSum of memory values: {sum(run_init_program_v2(instructions))}')

