# Day 6 Advent of Code
# Check customs declaration forms
file_name = "input/input_day_6.txt"


def count_group_unique_answers(group):
    """
    :param group: Group of customs forms
    :return: Number of unique answers filled in by group
    """
    group = group.replace('\n', '')
    return len(set(group))


def count_group_matching_answers(group):
    """
    :param group: Group of customs forms
    :return: Number of matching answers given on all forms in group
    """
    forms = group.split('\n')
    matching_answers = set(forms[0])
    for form in forms:
        matching_answers = matching_answers.intersection(set(form))
    return len(matching_answers)


if __name__ == '__main__':
    with open(file_name) as f:
        groups = f.read().split('\n\n')
        print(f'Sum of unique answers of every group: {sum(map(count_group_unique_answers, groups))}')
        print(f'Sum of same answers of every group: {sum(map(count_group_matching_answers, groups))}')
    f.close()

