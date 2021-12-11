import ctypes


def make_cdll_from_so(so_path: str):
    mandlebrot_so = ctypes.CDLL(so_path)
    mandlebrot_function = mandlebrot_so.mandlebrot
    mandlebrot_function.argtypes = (ctypes.c_double, ctypes.c_double, ctypes.c_int)
    return mandlebrot_function


def call_mandlebrot_cdll(re: float, im: float, cdll, max_iterations=200) -> int:
    iterations = cdll(re, im, max_iterations)
    return iterations

def cbrot(re: float, im: float, max_iterations=200) -> int:
    so_file = './mandlebrot.so'
    mandlebrot_function = make_cdll_from_so(so_file)
    iterations = mandlebrot_function(re, im, max_iterations)
    return iterations

if __name__ == '__main__':
    so_file = './mandlebrot.so'
    cdll = make_cdll_from_so(so_file)
    print(call_mandlebrot_cdll(0,0,cdll))
    
    
