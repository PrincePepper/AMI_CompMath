import math

import numpy as np
from matplotlib import pyplot
from scipy.interpolate import Akima1DInterpolator

a = -1  # левая граница
b = 2  # правая граница
n = 3  # шаг
func = lambda x: math.exp(x) * math.cos(x)

x = np.linspace(a, b, n)
x2 = np.arange(a, b, 0.01)

y = np.array([])
for i in range(0, len(x)):
    y = np.append(y, func(x[i]))

y2 = Akima1DInterpolator(x, y)(x2)
pyplot.subplots()

pyplot.plot(x, y, 'go', label='точки')
pyplot.plot(x, y, label='интерполяции линейная')

y = np.array([])
for i in range(0, len(x2)):
    y = np.append(y, func(x2[i]))
pyplot.plot(x2, y, label='f(x)')

pyplot.plot(x2, y2, 'r-', label='интерполяции Акима')

pyplot.title('Проверка функции y=sin x+cos x на промежутке [-1;2]')
pyplot.xlabel(r'$x$', fontsize=10)
pyplot.ylabel(r'$f(x)$', fontsize=10)
pyplot.grid(True)
pyplot.legend(loc='best', fontsize=10)
pyplot.savefig('figure_n_' + str(n) + '.png')
pyplot.show()

# -----------------------------------------------------------------------------------
# Рисование всех 10 n-ок
#
# pyplot.ylim([1.550,1.552])
#
# x = np.linspace(a, b, 3)
# y = np.array([])
# for i in range(0, len(x)):
#     y = np.append(y, func(x[i]))
# y2 = Akima1DInterpolator(x, y)(x2)
# pyplot.plot(x2, y2, label='n=3')
#
# x = np.linspace(a, b, 4)
# y = np.array([])
# for i in range(0, len(x)):
#     y = np.append(y, func(x[i]))
# y2 = Akima1DInterpolator(x, y)(x2)
# pyplot.plot(x2, y2, label='n=4')
#
# x = np.linspace(a, b, 5)
# y = np.array([])
# for i in range(0, len(x)):
#     y = np.append(y, func(x[i]))
# y2 = Akima1DInterpolator(x, y)(x2)
# pyplot.plot(x2, y2, label='n=5')
#
# x = np.linspace(a, b, 6)
# y = np.array([])
# for i in range(0, len(x)):
#     y = np.append(y, func(x[i]))
# y2 = Akima1DInterpolator(x, y)(x2)
# pyplot.plot(x2, y2, label='n=6')
#
# x = np.linspace(a, b, 7)
# y = np.array([])
# for i in range(0, len(x)):
#     y = np.append(y, func(x[i]))
# y2 = Akima1DInterpolator(x, y)(x2)
# pyplot.plot(x2, y2, label='n=7')
#
# x = np.linspace(a, b, 8)
# y = np.array([])
# for i in range(0, len(x)):
#     y = np.append(y, func(x[i]))
# y2 = Akima1DInterpolator(x, y)(x2)
# pyplot.plot(x2, y2, label='n=8')
#
# x = np.linspace(a, b, 9)
# y = np.array([])
# for i in range(0, len(x)):
#     y = np.append(y, func(x[i]))
# y2 = Akima1DInterpolator(x, y)(x2)
# pyplot.plot(x2, y2, label='n=9')
#
# x = np.linspace(a, b, 10)
# y = np.array([])
# for i in range(0, len(x)):
#     y = np.append(y, func(x[i]))
# y2 = Akima1DInterpolator(x, y)(x2)
# pyplot.plot(x2, y2, label='n=10')
#
# y = np.array([])
# for i in range(0, len(x2)):
#     y = np.append(y, func(x2[i]))
# pyplot.plot(x2, y, label='f(x)')
#
# pyplot.title('Проверка функции y=sin x+cos x на промежутке [-1;2]')
# pyplot.xlabel(r'$x$', fontsize=10)
# pyplot.ylabel(r'$f(x)$', fontsize=10)
# pyplot.grid(True)
# pyplot.legend(loc='best', fontsize=10)
# pyplot.show()
#
