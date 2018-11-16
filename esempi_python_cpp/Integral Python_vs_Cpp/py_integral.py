'''
Python
'''

def py_f(x: float) -> float:
    return x * x + x

def py_integral(a: float, b: float, n: int) -> float:
    """
    Estimate the area beneath the curve py_f, between the
    abscissas a and b; the region is approximated as n rectangles.
    """
    total = 0.0
    dx = (b - a) / n
    for i in range(n):
        total += dx * py_f(a + dx * i)
    return total
