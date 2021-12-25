import ctypes
import math
import multiprocessing as mp
# shared_memory is implemented in python3.8
# at the time of writing, Debian stable is still on 3.7
# it's okay, I've always wanted to try functional programming I guess
# from multiprocessing import shared_memory 
from multiprocessing import sharedctypes
import numpy as np
from time import time
from sys import argv
global size
size = int(argv[1])


def square_row(vector) -> None:
    for x in range(len(vector)):
        vector[x] = x+x+x


def make_value(i):
    for i in range(100):
        x = i + math.sqrt(i)
    return i

def set_value(index: int):
    for i in range(100):
        x = i + math.sqrt(i)
    return index

def set_shared_value(array, index: int):
    array[index] = index

def single_core_run():
    array = [0.0] * (size*size)
    print(array[0:5])
    time1 = time()
    for i in range(len(array)):
        array[i] = set_value(i)
    time2 = time()
    print(array[0:5])
    print(f'single run time: {time2 - time1}')


def multi_core_run():
    pool = mp.Pool(processes=3)
    array = [0.0] * (size*size)
    print(array[0:5])
    time1 = time()
    array = pool.map(set_value, range(len(array)))
    pool.close()
    pool.join()
    time2 = time()
    print(array[0:5])
    print(f'multiple run time: {time2 - time1}')


#matrix = np.zeros((10000,10000))
#start_single = time()
#for row in matrix:
    #square_row(row)
#stop_single = time()
#print(f'single process time: {stop_single-start_single}')
#matrix = np.zeros((10000,10000))
#pool = mp.Pool(16)
#start_multi = time()
#pool.map(square_row, matrix)
#stop_multi = time()
#print(f'multi process time: {stop_multi-start_multi}')
#pool.close()
#pool.join()
single_core_run()
multi_core_run()





