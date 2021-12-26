from ctype_test.cbrot import make_cdll_from_so
from ctype_test.cbrot import make_normalized_cdll_from_so 
from ctype_test.cbrot import call_mandlebrot_cdll
import ctypes
from helpers.data import y_index
import multiprocessing as mp
import multiprocessing.shared_memory
import numpy as np
from objects.task import Task
from result import Result
from sys import argv
from time import time


def calculate_row(array: np.array) -> None:
    """Runs the given function on every value in the array. No return value."""
    c_imaginary = array[0]  # y-value
    length = len(array)
    _step = 4 / length
    #print(_step)
    for point in range(length):
        c_real = -2 + point * _step  # x-value
        array[point] = mandlebrot_function(c_real, c_imaginary, job.max_iterations, job.escape_value) 
        

def run_job(job: Task) -> Result:
    """Unpacks a task object and runs the appropriate fucntions on it, then
    returns the result."""
    response = Result(job)
    horizontal_length = int(4 / job.step)
    vertical_height = int(-(job.end - job.start) / job.step)
    chunk = vertical_height/4
    print(f'x length: {horizontal_length}')
    print(f'y length: {vertical_height}')
    matrix = np.zeros((vertical_height, horizontal_length))
    time1 = time()
    y_index(matrix, job.step)
    for row in matrix:
        calculate_row(row)
    time2 = time()
    print(matrix[0])
    print(f'single process: {time2-time1}')
    time3 = time()
    shared_memory = mp.shared_memory.SharedMemory(name='test', create=True, size=8*horizontal_length*vertical_height)
    matrix = np.ndarray((vertical_height, horizontal_length), buffer=shared_memory.buf)
    y_index(matrix, job.step)
    pool = mp.Pool()
    pool.map(calculate_row, matrix)
    time4 = time()
    print(matrix[0])
    print(f'multi process: {time4-time3}')
    response.result = response
    shared_memory.close()
    shared_memory.unlink()
    pool.terminate()
    pool.close()
    return response


def main(argv):
    global job
    job = Task(2.0, -2.0, 200, 0.001, 10000)
    global mandlebrot_function
    mandlebrot_function = make_normalized_cdll_from_so('ctype_test/mandlebrot.so')
    response = run_job(job)


if __name__ == '__main__':
    main(argv)


