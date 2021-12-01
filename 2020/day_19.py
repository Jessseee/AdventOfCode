# Day 19 Advent of Code
# Here there be sea monsters
from helpers import *
import re


def parse_rule(rule, rules, found):
    pattern = ''
    if rule[0] in ['a', 'b']:
        return rule[0]
    pattern += '('
    for i, rev in enumerate(rule):
        if rev == '|':
            pattern += '|'
        else:
            if rev in found:
                rev_pattern = found[rev]
            else:
                rev_pattern = parse_rule(rules.get(rev), rules, found)
                found[rev] = rev_pattern
                print(color_text(f'{rev}\t\t{rules.get(rev)}:\t', 37), rev_pattern)
            pattern += rev_pattern
    pattern += ')'
    return pattern


def apply_rule(rule_regex, messages):
    return sum([re.match(rule_regex, message) is not None for message in messages])


if __name__ == '__main__':
    # rules = {'0': ['4', '1', '5'], '1': ['2', '3', '|', '3', '2'], '2': ['4', '4', '|', '5', '5'], '3': ['4', '5', '|', '5', '4'], '4': ['a'], '5': ['b']}
    # messages = ['ababbb', 'bababa', 'abbbab', 'aaabbb', 'aaaabbb']
    rules, messages = import_input().read().split('\n\n')
    rules = {index: nums.split(' ') for index, nums in [rule.split(': ') for rule in rules.replace('"', '').split('\n')]}

    rule_pattern = parse_rule(rules['0'], rules, {})
    rule_regex = re.compile(rule_pattern)
    print(f"0\t\t{rules.get('0')}\t", rule_pattern)
    print(len(messages))
    print(apply_rule(rule_regex, messages))
