# Day 16 Advent of Code
# Train Ticket business
import re

import more_itertools as itr

from aoc.helpers import *


def scan_tickets(tickets, rules):
    valid_tickets = tickets.copy()
    invalid_values = []
    for ticket in tickets:
        for ticket_value in ticket:
            eval_ticket_value = [
                not (r[0] <= ticket_value <= r[1] or r[2] <= ticket_value <= r[3]) for r in rules.values()
            ]
            if all(eval_ticket_value):
                invalid_values.append(ticket_value)
                valid_tickets.remove(ticket)
    return valid_tickets, invalid_values


def check_field_position(tickets, rules):
    possible_fields = {}
    for i in range(len(rules)):
        possible_fields[i] = []
        tickets_field_i = [ticket[i] for ticket in tickets]
        for name, r in rules.items():
            eval_ticket_values = [
                r[0] <= ticket_field_i <= r[1] or r[2] <= ticket_field_i <= r[3] for ticket_field_i in tickets_field_i
            ]
            if all(eval_ticket_values):
                possible_fields[i].append(name)

    taken = []
    for key in sorted(possible_fields, key=lambda key: len(possible_fields[key])):
        for name in taken:
            possible_fields[key].remove(name)
        for name in possible_fields[key]:
            taken.append(name)

    ticket_fields = [value[0] for value in possible_fields.values()]
    print(f"Order of ticket field names: {ticket_fields}")
    return ticket_fields


def check_departure_fields(ticket, ticket_fields):
    fields = []
    for i, ticket_field in enumerate(ticket_fields):
        if ticket_field.startswith("departure"):
            fields.append(ticket[i])
    result = 1
    for x in fields:
        result *= x
    return result


if __name__ == "__main__":
    input = import_input().read().split("\n\n")

    rules = {}
    for rule in input[0].split("\n"):
        match = re.match(r"([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)", rule)
        name, r1_min, r1_max, r2_min, r2_max = match.groups()
        rules[name] = list(map(int, [r1_min, r1_max, r2_min, r2_max]))

    my_ticket = input[1].split(":\n")[1].split(",")
    my_ticket = list(map(int, my_ticket))

    nearby_tickets = input[2].split(":\n")[1].replace("\n", ",").split(",")
    nearby_tickets = map(int, nearby_tickets)
    nearby_tickets = list(itr.grouper(nearby_tickets, len(rules)))

    valid_tickets, invalid_values = scan_tickets(nearby_tickets, rules)
    print(f"Scan error rate: {sum(invalid_values)}")
    ticket_fields = check_field_position(valid_tickets, rules)
    print(f"Product of departure fields: {check_departure_fields(my_ticket, ticket_fields)}")
