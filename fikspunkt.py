import numpy as np
from sympy import *


def f(x): 
    return x**4 - 9*x**3 + 27*x**2 - 31*x + 12


def newt(x):
    z = 1000
    while abs(x-z) > 0.00005:
        z = x
        x = x - (f(x) / (4*x**3 - 27*x**2 + 54*x - 31))
    return x



solutions = []
for i in range(-25, 25):
    try:
        newt(i)
    except ZeroDivisionError:
        pass
    else:
        x = newt(i)
        if round(x, 4) not in solutions:
            solutions.append(round(x,4))


print(solutions)




