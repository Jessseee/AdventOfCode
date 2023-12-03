# Day 10 of Advent of Code 2021
# Syntax Scoring

# We asked the submarine to determine the best route out of the deep-sea cave, but it only replies:
# ---- Syntax error in navigation subsystem on line: ALL OF THEM ----
# The damage is worse than expected, luckily we have a copy of the navigation subsystem source code.

# The navigation subsystem syntax is made of several lines containing chunks.
# There are one or more chunks on each line, and chunks contain zero or more other chunks.
# Adjacent chunks are not separated by any delimiter; if one chunk stops, the next chunk
# (if any) can immediately start. Every chunk must open and close with one of
# four legal pairs of matching characters:

# If a chunk opens with (, it must close with ).
# If a chunk opens with [, it must close with ].
# If a chunk opens with {, it must close with }.
# If a chunk opens with <, it must close with >.

# Some lines are incomplete, but others are corrupted.

# A corrupted line is one where a chunk closes with the wrong character. These must be discarded.
# We can calculate a syntax error score for a line, by taking the first illegal character on the
# line and look it up in the following table:
# ): 3 points.
# ]: 57 points.
# }: 1197 points.
# >: 25137 points.

# An incomplete line on the other hand can be repaired with the correct sequence of closing characters.
# We can also calculate an autocomplete score for these completion sequences by starting with a total score of 0.
# Then, for each character, multiplying the total score by 5 and finally increase the total score by the point value
# given for the character in the following table
# ): 1 point.
# ]: 2 points.
# }: 3 points.
# >: 4 points.
# The winning competed line is found by sorting all the autocomplete scores and then taking the middle score.

from aoc.helpers import *

tags = {("(", ")"): (3, 1), ("[", "]"): (57, 2), ("{", "}"): (1197, 3), ("<", ">"): (25137, 4)}


if __name__ == "__main__":
    source = import_input("\n", example=False)
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
                # For each opening tag keep track of the opened chunks
                # and the matching closing tags for the autocompletion.
                if tag == opening:
                    opened.insert(0, opening)
                    complete.insert(0, closing)
                    break
                # For each closing tag we first check if it is valid.
                if tag == closing:
                    # If the closing line does not match the tag of the last
                    # opened chunk mark the line as corrupted.
                    if opening != opened[0]:
                        corrupted = True
                        error_scores += error_score
                    # Remove the opening tag from the list of opened chunks
                    else:
                        opened.remove(opening)
                        complete.remove(closing)
                    break

        # if the line is not corrupted we calculate the completion score3
        if not corrupted:
            for tag in complete:
                for (_, closing), (_, completion_score) in tags.items():
                    if tag == closing:
                        complete_score *= 5
                        complete_score += completion_score
            completion_scores.append(complete_score)

    completion_score = sorted(completion_scores)[len(completion_scores) // 2]
    print(f"The total error score is: {c('{:,}'.format(error_scores), 31)}")
    print(f"The total completions score is: {c('{:,}'.format(completion_score), 31)}")
