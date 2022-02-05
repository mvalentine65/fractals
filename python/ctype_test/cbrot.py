"""
This module loads a shared object into python. The
shared object can then be used to caculate the mandelbrot
set with compiled code instead of python.
"""

import ctypes


def make_cdll_from_so(so_path: str):
    """Makes a cdll out of the specified file. Argument should be a
    .so file. Returns the mandelbrot function from the .so file."""
    mandelbrot_so = ctypes.CDLL(so_path)
    mandelbrot_function = mandelbrot_so.mandelbrot
    mandelbrot_function.argtypes = (ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_int)
    return mandelbrot_function


def make_normalized_cdll_from_so(so_path: str):
    """Makes a cdll out of the specified shared object file.
    Returns the log normalized mandelbrot function."""
    mandelbrot_so = ctypes.CDLL(so_path)
    mandelbrot_function = mandelbrot_so.mandelbrot_log_normalized
    mandelbrot_function.argtypes = (ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_int)
    mandelbrot_function.restype = ctypes.c_double
    return mandelbrot_function


def make_char_mandelbrot(so_path:str):
    """Makes a cdll out of the specified shared object file.
    The generated mandelbrot function returns an unsigned char
    to minimize memory use."""
    mandelbrot_so = ctypes.CDLL(so_path)
    mandelbrot_function = mandelbrot_so.mandelbrot
    mandelbrot_function.argtypes = (ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_int)
    mandelbrot_function.restype = ctypes.c_ubyte
    return mandelbrot_function



def call_mandelbrot_cdll(re: float, im: float, cdll, max_iterations=200, escape_value=4) -> int:
    """Calls the provided mandelbrot cdll with the supplied arguments. Re is the
    real component of C. Im is the imaginary component of C. Returns the iterations
    as an int."""
    iterations = cdll(re, im, max_iterations, escape_value)
    return iterations


def cbrot(re: float, im: float, max_iterations=200) -> int:
    """Creates a cdll from mandelbrot.so and runs the function. Returns the
    number of iterations performed as an int."""
    so_file = './mandelbrot.so'
    mandelbrot_function = make_cdll_from_so(so_file)
    iterations = mandelbrot_function(re, im, max_iterations, 4)
    return iterations


if __name__ == '__main__':
    so_file = './mandelbrot.so'
    cdll = make_cdll_from_so(so_file)
    print(call_mandelbrot_cdll(0,0,cdll))
    
    
