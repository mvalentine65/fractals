import timeit
from get_iter import get_iter
from cbrot import cbrot
import sys

runs = int(sys.argv[1])

def f1():
    c = complex(0,0)
    get_iter(c, max_steps=200)

def f2():
    cbrot(0.0,0.0,200)

if __name__ == '__main__':
    python_time = timeit.timeit(f1, number=runs)
    ctype_time = timeit.timeit(f2, number=runs)
    print(f'pure python time: {python_time}')
    print(f'ctype time: {ctype_time}')
