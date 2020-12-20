# Day 18 Advent of Code
# Weird maths
from helpers import *
import regex


def solve_exp_with_parens(exp, solve_exp):
    solved_blocks = {}
    print(exp, '\n')
    blocks = regex.findall(r'\((?:[^()]++|(?0))++\)', exp)
    for i, block in enumerate(blocks):
        if '(' in block[1:-1]:
            solved_blocks[block] = solve_exp_with_parens(block[1:-1], solve_exp)
        else:
            solved_blocks[block] = solve_exp(block[1:-1])
        print()
    for block, solution in solved_blocks.items():
        exp = exp.replace(block, solution)
    return solve_exp(exp)


def solve_exp_ltr(exp):
    prev_result = regex.findall(r'\d+', exp)[0]
    for opr in regex.findall(r' [*+] \d+', exp):
        opr = prev_result + opr
        prev_result = str(eval(opr))
    return prev_result


def solve_exp_addition_first(exp):
    print(exp)
    if '*' not in exp or '+' not in exp:
        print(eval(exp))
        return str(eval(exp))

    opr = regex.search(r'(\d+ \+ \d+)', exp)
    result = str(eval(opr.group()))
    exp = replace_chrs(opr.span(), result, exp)

    return solve_exp_addition_first(exp)


if __name__ == '__main__':
    input = import_input().read().split('\n')
    example_input = [
        "9 + 14 * 19 + 14",
        "1 + (2 * 3) + (4 * (5 + 6))",  # = 51
        "2 * 3 + (4 * 5)",  # = 46
        "5 + (8 * 3 + 9 + 3 * 4 * 3)",  # = 1445
        "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",  # = 669060
    ]

    results = []
    for expression in input:
        results.append(solve_exp_with_parens(expression, solve_exp_addition_first))
        print(color_text(f"\n{expression} = {results[-1]}\n\n", 32))
    print(f'Sum of all results: {sum(list(map(int, results)))}')
