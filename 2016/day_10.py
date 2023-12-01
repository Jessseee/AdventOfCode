# Day <DAY> of Advent of Code <YEAR>
# <PUZZLE TITLE>
from helpers import *
from collections import defaultdict
from dataclasses import dataclass, field


def parse_target(target):
    type, index = target.split(" ")
    return bots[int(index)] if type == 'bot' else outputs[int(index)]


@dataclass
class Output:
    chips: list[int] = field(default_factory=list)


@dataclass
class Bot(Output):
    target_low: Output = None
    target_high: Output = None

    def move(self):
        self.target_low.chips.append(min(self.chips))
        self.target_high.chips.append(max(self.chips))
        self.chips = []


if __name__ == '__main__':
    inputs = import_input('\n', example=False)
    bots = defaultdict(Bot)
    outputs = defaultdict(Output)
    for instruction in inputs:
        if assign := re.findall(r"value (\d+) .* bot (\d+)", instruction):
            chip, index = list(map(int, assign[0]))
            bots[index].chips.append(chip)
        if handover := re.findall(r"(bot \d+) .* ((?:bot|output) \d+) .* ((?:bot|output) \d+)", instruction):
            source, target_low, target_high = [parse_target(x) for x in handover[0]]
            source.target_low = target_low
            source.target_high = target_high
    while any(len(bot.chips) == 2 for bot in bots.values()):
        for index, bot in bots.items():
            if len(bot.chips) == 2:
                if [17, 61] == bot.chips:
                    print("Bot that handled chips 17 and 61: ", index)
                bot.move()
    print("outputs:", sorted(outputs.items()))
