# some utility function for displaying data.
import matplotlib.pyplot as plt


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


def color_text(text, color_code):
    """
    Color text for display in console using ANSI escape sequence.

    :param Any text: The text to be colored.
    :param int color_code: The ANSI color code.
    :return: ANSI escape sequence.
    """
    return f'\033[{color_code}m{str(text)}\033[0m'
