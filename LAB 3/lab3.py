import math

import numpy as np


# https://coderoad.ru/14823891/%D0%98%D0%BD%D1%82%D0%B5%D1%80%D0%BF%D0%BE%D0%BB%D0%B8%D1%80%D1%83%D1%8E%D1%89%D0%B8%D0%B9-%D0%BF%D0%BE%D0%BB%D0%B8%D0%BD%D0%BE%D0%BC-%D0%9D%D1%8C%D1%8E%D1%82%D0%BE%D0%BD%D0%B0-python
def coef(x, y):
    '''x : array of data points
       y : array of f(x)  '''
    x.astype(float)
    y.astype(float)
    n = len(x)
    a = []
    for i in range(n):
        a.append(y[i])

    for j in range(1, n):

        for i in range(n - 1, j - 1, -1):
            a[i] = float(a[i] - a[i - 1]) / float(x[i] - x[i - j])

    return np.array(a)  # return an array of coefficient


def Eval(a, x, r):
    ''' a : array returned by function coef()
       x : array of data points
       r : the node to interpolate at  '''

    x.astype(float)
    n = len(a) - 1
    temp = a[n] + (r - x[n])
    for i in range(n - 1, -1, -1):
        temp = temp * (r - x[i]) + a[i]
    return temp  # return the y_value interpolation


# 1-я формула Ньютона
def first_newton_f():
    return


# 2-я формула Ньютона
def second_newton_f():
    pass


# 1-я формула Гаусса
def first_gauss_f():
    pass


# 2-я формула Гаусса
def second_gauss_f():
    pass


# Формула Стирлинга
def stirling_f():
    pass


# Формула Бесселя
def bessel_f():
    pass


def my_function(x):
    return x ** 2 + math.log10(x)


a = 0.4  # левая граница
b = 0.9  # правая граница
h = (b - a) / 10  # шаг
x_star = 0.53  #

mass_function_x = []
for i in range(0, 11):
    mass_function_x.append(a + i * h)
print(*mass_function_x)

# ---------------------------------------------------------------------------
# находим ближайщее значение к нашему x, а затем xᵢ₊₁ и xᵢ₋₁
x_i = sorted(mass_function_x, key=lambda x: abs(x_star - x))[0]
x_i_next = sorted(mass_function_x, key=lambda x: abs(x_star - x))[1]
x_i_back = sorted(mass_function_x, key=lambda x: abs(x_star - x))[2]
print("xi:", x_i, " ", "xi+1:", " ", x_i_next, "xi-1:", x_i_back)

# ---------------------------------------------------------------------------

next = my_function(x_i_next)
now = my_function(x_i)
forward = my_function(x_i_back)
y = np.array([next, now, forward])
x = np.array([x_i_next, x_i, x_i_back])

aaa = coef(x, y)
print(aaa)

next = my_function(x_i_next)
now = my_function(x_i)
forward = my_function(x_i_back)

f_1 = (now - next) / (x_i - x_i_next)
f_2 = (forward - now) / (x_i_back - x_i)
f_3 = (f_1 - f_2) / (x_i_next - x_i_back)
print(f_1, f_2, f_3)
