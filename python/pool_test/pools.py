import multiprocessing as mp
import numpy as np
from time import time


def square_row(vector) -> None:
    for x in range(len(vector)):
        vector[x] = x+x+x




matrix = np.zeros((10000,10000))
start_single = time()
for row in matrix:
    square_row(row)
stop_single = time()
print(f'single process time: {stop_single-start_single}')
matrix = np.zeros((10000,10000))
pool = mp.Pool(16)
start_multi = time()
pool.map(square_row, matrix)
stop_multi = time()
print(f'multi process time: {stop_multi-start_multi}')
pool.close()
pool.join()









