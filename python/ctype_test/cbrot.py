import ctypes
import numpy as np

def cbrot(re: float, im: float, max_iterations=200):
    so_file = './mandlebrot.so'
    mandlebrot_so = ctypes.CDLL(so_file)
    mandlebrot_function = mandlebrot_so.mandlebrot
    mandlebrot_function.argtypes = (ctypes.c_double, ctypes.c_double, ctypes.c_int)
    iterations = mandlebrot_function(re, im, max_iterations)
    return iterations
