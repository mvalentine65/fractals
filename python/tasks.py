import argparse
from celery import Celery
import matplotlib.pyplot as plot
import numpy as np

app = Celery('tasks', backend='rpc://', broker='pyamqp://192.168.137.11//')


def make_axis_values(number: int, start=2, stop=-2) -> np.array:
    axis = np.linspace(start, stop, number)
    return axis


def get_iter(vals:tuple) -> int:
    # Z_(n) = (Z_(n-1))^2 + c
    # Z_(0) = c
    y, x = vals
    c = complex(x, y)
    z=c
    i=1
    while i<100 and (z*z.conjugate()).real<4:
        z=z*z +c
        i+=1
    return i


@app.task
def make_row(y: float, length: int, escape: int, max_steps: int, x_max=2, x_min=-2):
    x_axis = make_axis_values(length, start=x_min, stop=x_max)
    for i,x in enumerate(x_axis):
        x_axis[i] = get_iter((y,x))
    return list(x_axis)


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
    picture = [[]*number]
    for index in range(number):
        y = y_values[index]
        result = tasks.make_row.delay(y, number, args.x_max, args.y_max)
        picture[index]=result.get()
    pyplot.imshow(picture, colormap=args.colormap)
    pyplot.show()
    
