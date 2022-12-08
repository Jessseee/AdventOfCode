# some utility function for displaying data.
import matplotlib.pyplot as plt
from enum import Enum


def print_2d_array(array, el_length=1):
    """
    Nicely print a 2d array.

    :param list[list]|ndarray array: 2d array to print.
    :param int el_length: the length of each element in the array.
    """
    for row in array:
        for el in row:
            if not el:
                print(' '*(el_length-1) + '.', end=' ')
            else:
                print(str(el).zfill(el_length), end=' ')
        print()


def plot_3d_array(array):
    """
    Plot a 3d array using pyplot.

    :param array: 3d array to plot.
    """
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(*zip(*array))
    plt.show()


Color = Enum('Color', ['BLACK', 'RED', 'GREEN', 'ORANGE', 'BLUE', 'PURPLE', 'CYAN', 'GREY'], start=30)
Highlight = Enum('Highlight', ['BLACK', 'RED', 'GREEN', 'ORANGE', 'BLUE', 'PURPLE', 'CYAN', 'GREY'], start=30)
Effect = Enum('Effect', zip(['BOLD', 'ITALIC', 'STRIKE', 'UNDERLINE'], [1, 3, 9, 21]))


def color_text(text, effect):
    """
    Color text for display in console using ANSI escape sequence.

    :param Any text: The text to be colored.
    :param int effect: The ANSI code or related Enum value.
    :return: ANSI escape sequence.
    """
    if isinstance(effect, (Color, Highlight, Effect)): effect = effect.value
    return f'\033[{effect}m{str(text)}\033[0m'


def result(text):
    return color_text(text, Color.GREEN)
