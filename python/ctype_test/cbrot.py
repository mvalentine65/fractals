"""
This module loads a shared object into python. The
shared object can then be used to caculate the mandlebrot
set with compiled code instead of python.
"""

import ctypes


def make_cdll_from_so(so_path: str):
    """Makes a cdll out of the specified file. Argument should be a
    .so file. Returns the mandlebrot function from the .so file."""
    mandlebrot_so = ctypes.CDLL(so_path)
    mandlebrot_function = mandlebrot_so.mandlebrot
    mandlebrot_function.argtypes = (ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_int)
    return mandlebrot_function


def make_normalized_cdll_from_so(so_path: str):
    """Makes a cdll out of the specified shared object file.
    Returns the log normalized mandlebrot function."""
    mandlebrot_so = ctypes.CDLL(so_path)
    mandlebrot_function = mandlebrot_so.mandlebrot_log_normalized
    mandlebrot_function.argtypes = (ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_int)
    mandlebrot_function.restype = ctypes.c_double
    return mandlebrot_function


def call_mandlebrot_cdll(re: float, im: float, cdll, max_iterations=200, escape_value=4) -> int:
    """Calls the provided mandlebrot cdll with the supplied arguments. Re is the
    real component of C. Im is the imaginary component of C. Returns the iterations
    as an int."""
    iterations = cdll(re, im, max_iterations, escape_value)
    return iterations


def cbrot(re: float, im: float, max_iterations=200) -> int:
    """Creates a cdll from mandlebrot.so and runs the function. Returns the
    number of iterations performed as an int."""
    so_file = './mandlebrot.so'
    mandlebrot_function = make_cdll_from_so(so_file)
    iterations = mandlebrot_function(re, im, max_iterations)
    return iterations


if __name__ == '__main__':
    so_file = './mandlebrot.so'
    cdll = make_cdll_from_so(so_file)
    print(call_mandlebrot_cdll(0,0,cdll))
    
    
