"""Used as a benchmark and for testing the shared object's output.
Borrowed from https://levelup.gitconnected.com/mandelbrot-set-with-python-983e9fc47f56"""
def get_iter(c:complex, thresh:int =4, max_steps:int =25) -> int:
    # Z_(n) = (Z_(n-1))^2 + c
    # Z_(0) = c
    z=c
    i=1
    while i<max_steps and (z*z.conjugate()).real<thresh:
        z=z*z +c
        i+=1
    return i

