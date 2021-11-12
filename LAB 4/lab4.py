import math

import scipy
from scipy.misc import derivative


def func_der(x):
    return 2 * x + 1 / (math.log(10) * x)


def Solve(x):
    return x ** 2 + math.log10(x)


def Lagrange(x):
    return Solve(x0) * ((x - x1) * (x - x2) * (x - x3)) / ((x0 - x1) * (x0 - x2) * (x0 - x3)) + \
           Solve(x1) * ((x - x0) * (x - x2) * (x - x3)) / ((x1 - x0) * (x1 - x2) * (x1 - x3)) + \
           Solve(x2) * ((x - x0) * (x - x1) * (x - x3)) / ((x2 - x0) * (x2 - x1) * (x2 - x3)) + \
           Solve(x3) * ((x - x0) * (x - x1) * (x - x2)) / ((x3 - x0) * (x3 - x1) * (x3 - x2))


def der_lagrange(x):
    return scipy.misc.derivative(Lagrange, x, dx=1e-6)


a = 0.4  # левая граница
b = 0.9  # правая граница
x0 = 0.4
x1 = 0.45
x2 = 0.5
x3 = 0.55

h = (b - a) / 10
xx = [a + i * h for i in range(11)]
print(xx)
# ---------------------------------------------------------------------------

print(der_lagrange(x3))
print(func_der(x3))
print(der_lagrange(x3) - func_der(x3))
