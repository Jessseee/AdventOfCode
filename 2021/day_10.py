# Day 10 of Advent of Code 2021
# Syntax Scoring
from helpers import *

tags = {
    ('(', ')'): (3, 1),
    ('[', ']'): (57, 2),
    ('{', '}'): (1197, 3),
    ('<', '>'): (25137, 4)
}


if __name__ == '__main__':
    source = import_input('\n', example=False)
    error_scores = 0
    completion_scores = []
    for line in source:
        complete_score = 0
        opened = []
        complete = []
        corrupted = False
        for tag in line:
            if corrupted:
                break
            for (opening, closing), (error_score, _) in tags.items():
                if tag == opening:
                    opened.insert(0, opening)
                    complete.insert(0, closing)
                    break
                if tag == closing:
                    if opening != opened[0]:
                        corrupted = True
                        error_scores += error_score
                    else:
                        opened.remove(opening)
                        complete.remove(closing)
                    break
        if not corrupted:
            for tag in complete:
                for (_, closing), (_, completion_score) in tags.items():
                    if tag == closing:
                        complete_score *= 5
                        complete_score += completion_score
            completion_scores.append(complete_score)
    completion_score = sorted(completion_scores)[len(completion_scores) // 2]
    print(f"The total error score is: {color_text('{:,}'.format(error_scores), 31)}")
    print(f"The total completions score is: {color_text('{:,}'.format(completion_score), 31)}")
