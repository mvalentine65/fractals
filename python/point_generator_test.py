from helpers.data import y_index
from helpers.data import make_matrix
import multiprocessing as multi
import numpy as np
from sys import argv
from matplotlib import pyplot as plt


def stepper(step: float) -> float:
    """generator object for the x values"""
    value = 0
    while True:
        yield value % 4
        value += step


def make_row(array):
    length = len(array)
    delta = 4 / length
    for x in range(length):
        value = x * delta
        for i in range(200):
            if value > 10:
                array[x] = value
                break
        if array[x] == 0:
            array[x] == 200
    return array


def get_iter(vals:tuple, thresh:int =4, max_steps:int =50) -> int:
    # Z_(n) = (Z_(n-1))^2 + c
    # Z_(0) = c
    y, x = vals
    c = complex(x, y)
    z=c
    i=1
    while i<max_steps and (z*z.conjugate()).real<thresh:
        z=z*z +c
        i+=1
    return i


def arg_generator(step: float) -> tuple:
    points = np.linspace(2,-2,int(4/step))
    for y in points:
        for x in points[::-1]:
            yield (y,x)

        

def main(argv):
    step = float(argv[1])
    number_of_points = int(4/step)
    shape = (number_of_points, number_of_points) 
    #values = (y//200 for y in range(40000))
    args = arg_generator(step)
    #print(matrix)
    pool = multi.Pool()
    matrix = np.array([5])
    print(matrix[0])
    matrix = np.array(pool.map(get_iter, args))
    matrix = np.reshape(matrix, shape)
    print(matrix)
    print(type(matrix[0]))
    pool.close()
    pool.join()
    plt.imshow(matrix)
    plt.savefig('pool-map-test.png')
    #gen = stepper(0.02)
    #array = list()
    #number = int(4/0.02)
    #for i in range(number):
     #   array.append(gen.__next__())
    #print(array)

if __name__ == '__main__':
    main(argv)
