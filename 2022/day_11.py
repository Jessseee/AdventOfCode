# Day 11 of Advent of Code 2022
# Monkey in the Middle

# A couple of monkeys have stolen some of our supplies. To get our stuff back we need to
# predict where the monkeys will throw the items. It appears that the monkeys operate based
# on how worried we are about our specific items. Each monkey influences how worried we are
# about an item differently. With this information we can find which monkeys handle our
# items most often while throwing them back and forth. Our job is to calculate the amount
# of monkey business (product of times handling our items for the two most active monkeys).

from helpers import *
from copy import deepcopy
import math
import re


class Monkey:
    def __init__(self, id, starting_items, operation, test, if_true, if_false):
        self.id = id
        self.held_items = list(map(int, starting_items.split(', ')))
        self.current_item = None
        self.operation = lambda old: eval(operation.split('= ')[1])
        self.divisor = int(test.split('by ')[1])
        if_true = int(if_true.split('monkey ')[1])
        if_false = int(if_false.split('monkey ')[1])
        self.test = lambda item: if_true if item % self.divisor == 0 else if_false
        self.inspected = 0

    def inspect(self, reducer):
        while len(self.held_items) > 0:
            self.current_item = self.held_items.pop(0)
            self.current_item = self.operation(self.current_item)
            self.inspected += 1
            self.current_item = reducer(self.current_item)
            yield self.test(self.current_item)

    def throw(self):
        return self.current_item

    def catch(self, item):
        self.held_items.append(item)

    def __repr__(self):
        return f"Monkey {self.id}: {self.held_items}"


def parse_monkeys(data):
    id = re.findall(r'Monkey (\d+):', data)[0]
    properties = re.findall(r' +(.*): (.*)', data)
    return Monkey(id=id, **{key.lower().replace(' ', '_'): value for key, value in properties})


def monkey_business(monkeys, reducer, rounds):
    for round in range(1, rounds + 1):
        print(f"\rdoing monkey business ({round}/{rounds} rounds)", end='')
        for monkey in monkeys:
            for target in monkey.inspect(reducer):
                item = monkey.throw()
                monkeys[target].catch(item)
    monkey_business = math.prod(sorted([monkey.inspected for monkey in monkeys])[-2:])
    print(f"\rMonkey business after {rounds} rounds: {result('{:,}'.format(monkey_business))}")


if __name__ == '__main__':
    monkeys = import_input('\n\n', parse_monkeys, example=False)
    divisor = math.prod([monkey.divisor for monkey in monkeys])
    monkey_business(deepcopy(monkeys), lambda item: item // 3, 20)
    monkey_business(deepcopy(monkeys), lambda item: item % divisor, 10000)
