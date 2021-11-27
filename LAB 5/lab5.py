import math


def solve(x):
    return x ** 2 + math.log10(x)


def find_x(a, b, t):
    return (a + b) / 2 + (a - b) * t / 2


def g_func(a, b):
    return ((b - a) / 2) * (solve(find_x(a, b, t1)) + solve(find_x(a, b, t2)))


def NK(a, b, c, n):
    h = (b - a) / n
    x = a
    k = 0
    I = 0
    while k <= n:
        I += c[k] * solve(x)
        x += h
        k += 1
    return (b - a) * I


a = 0.4  # левая граница
b = 0.9  # правая граница
t1 = -0.577350
t2 = 0.577350
eps = 0.001

m = (a + b) / 2

print("I_n=", g_func(a, b))
print("I_2n=", g_func(a, m) + g_func(m, b))
print("delta I=", g_func(a, b) - (g_func(a, m) + g_func(m, b)))
print(g_func(a, b) - (g_func(a, m) + g_func(m, b)) < eps)
print()
c = [1 / 8, 3 / 8, 3 / 8, 1 / 8]
n = 3

print("I_n=", NK(a, b, c, n))
print("I_2n=", NK(a, m, c, n) + NK(m, b, c, n))
print("delta I=", (NK(a, m, c, n) + NK(m, b, c, n)) - NK(a, b, c, n))
print((NK(a, m, c, n) + NK(m, b, c, n)) - NK(a, b, c, n) < eps)
