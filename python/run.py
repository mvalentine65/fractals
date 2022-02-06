import argparse
from celery import Celery
import numpy as np
import matplotlib.pyplot as pyplot
from tasks import *
from time import time


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--step', type=float, default=0.005,
            help='Value to increment each point')
    parser.add_argument('-i', '--iterations', type=int, default=100,
            help='Maximum number of iterations before point is considered in the set')
    parser.add_argument('--colormap', default='plasma',
            help='colormap for pyplot')
    parser.add_argument('--x-max', type=float, default=2)
    parser.add_argument('--x-min', type=float, default=-2)
    parser.add_argument('--y-max', type=float, default=2)
    parser.add_argument('--y-min', type=float, default=-2)

    args = parser.parse_args()

    number = int( (args.y_max-args.y_min) / args.step )
    y_values = make_axis_values(number, args.y_max, args.y_min)
    picture = list(y_values)
    start_time = time()
    for index in range(number):
        y = y_values[index]
        result = make_row.delay(y, number, args.x_max, args.y_max)
        picture[index]=result.get()
    end_time = time()
    print(end_time - start_time)
    pyplot.imshow(picture, cmap=args.colormap)
    pyplot.show()
