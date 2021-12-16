"""
Visualizes the mandlebrot set with the given width and height. Requires cbrot.py.
"""
import argparse
from ctype_test.cbrot import make_cdll_from_so
from ctype_test.cbrot import call_mandlebrot_cdll
from helpers import data
from matplotlib import pyplot as plt
import numpy as np
from sys import argv
import time


def get_data_matrix(step: float) -> np.matrix:
    """Returns a 2d numpy array of length 4//step."""
    matrix = data.make_matrix(step)
    return matrix


def get_mandlebrot_function():
    """Getter for mandlebrot function."""
    mandlebrot_function = make_cdll_from_so('ctype_test/mandlebrot.so')
    return mandlebrot_function
    

def make_plot():
    """Returns a pyplot plot object"""
    plot = plt.figure()
    return plot 


def find_value(function, real: float, imaginary: float, max_iterations: int) -> float:
    """Runs the provided function with the provided arguments. Returns the
    (found iterations / max_iterations) % 1 as a float."""
    value = function(real, imaginary, max_iterations)
    value = value / max_iterations
    value = 1 - value
    return value


def fill_graph(matrix: np.matrix, step: float, function, max_iterations: int) -> None:
    """Iterates over the given numpy matrix and replaces the existing
    values with the number of iterations at that x,y coodinate."""
    # x starts at -2, ends at 2
    # y starts at 2i, ends at -2i
    # x = -2 + step*index
    # y = 2 - step*index
    length = len(matrix)
    for y in range(length):
        imaginary_component = data.find_imaginary_component(step, y)
        for x in range(length):
            real_component = data.find_real_component(step, x)
            value = find_value(function, real_component, imaginary_component, max_iterations)
            matrix[y][x] = value


def main(argv):
    parser = argparse.ArgumentParser(
                description="Visualize the mandlebrot set with the given width and height")
    parser.add_argument('--width', type=int, default=8,
                        help='Width in inches.')
    parser.add_argument('--height', type=int, default=8,
                        help='Height in inches.')
    parser.add_argument('--step', type=float, default=0.02,
                        help="Increment for x and y values.")
    parser.add_argument('--max-iterations', type=int, default=200,
                        help="""Maximum number of iterations to try before a
                        starting value is considered in the set.""")
    args = parser.parse_args()
    mandlebrot_function = get_mandlebrot_function()
    data = get_data_matrix(args.step)
    time1 = time.time()
    fill_graph(data, args.step, mandlebrot_function, args.max_iterations)
    time2 = time.time()
    print(time2-time1)
    plt.imshow(data)
    time3 = time.time()
    plt.show()
    print(time3-time2)
    print(data)


if __name__ == '__main__':
    main(argv)
