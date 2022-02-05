def py_mandlebrot(re: float, im: float, max_iterations: int) -> int:
    x = complex(re, im)
    current = 0
    z = complex(0, 0)
    while current < max_iterations:
        current += 1
        z = z*z + x
        if (z*z.conjugate()).real > 4:
            break
    return current


if __name__ == '__main__':
    re = float(input("first number"))
    im = float(input("second number"))
    result = py_mandlebrot(re, im, 200)
    print(result)
