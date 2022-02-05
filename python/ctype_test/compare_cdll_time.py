from cbrot import *
from sys import argv
import time


runs = int(argv[1])

start_1 = time.time()
for i in range(runs):
    iteration = cbrot(0.0, 0.0, 200)
end_1 = time.time()
total = end_1 - start_1
print(f'cbrot time: {total}')
print(f'mean cbrot time for {runs} runs: {total/runs}')

start_2 = time.time()
cdll = make_cdll_from_so('./mandelbrot.so')
for i in range(runs):
    iteration = call_mandelbrot_cdll(0.0, 0.0, cdll, max_iterations=200, escape_value =4)
end_2 = time.time()
total = end_2 - start_2
print(f'seperated time: {total}')
print(f'mean seperated time for {runs} runs: {total/runs}')
