"""
Visualizes the mandlebrot set with the given width and height. Requires cbrot.py.
"""
import argparse
from ctype_test.cbrot import make_cdll_from_so
from ctype_test.cbrot import call_mandlebrot_cdll
from matplotlib import pyplot as plt
from sys import argv


def get_mandlebrot():
    """Getter for mandlebrot function."""
    mandlebrot_function = make_cdll_from_so('ctype_test/mandlebrot.so')
    return mandlebrot_function
    

def make_plot():
    """Returns a pyplot plot object"""
    plot = plt.figure()
    



def main(argv):
    parser = argparse.ArgumentParser(
                description="Visualize the mandlebrot set with the given width and height")
    #parser.add_argument('--width', type=int, default=400,
                        #help='Window width in pixels.')
    #parser.add_argument('--height', type=int, default=400,
                        #help='Window height in pixels.')
    args = parser.parse_args()
    mandlebrot = get_mandlebrot()
    graph = make_plot()

if __name__ == '__main__':
    main(argv)
