import math


# Рунге-Кутты 4 порядка
# f - дифференциальное уравнение, y - функция, x - переменная, h - шаг, N - количество
# возвращает массив, вычисленных y и x, количеством N
def RK4_step(f, y, x, h, N):
    y_mass = [y]
    x_mass = [x]
    for k in range(N):
        k1 = f(y, x)
        k2 = f(y + k1 / 2, x + h / 2)
        k3 = f(y + k2 / 2, x + h / 2)
        k4 = f(y + k3, x + h)
        y = y + (k1 + 2 * k2 + 2 * k3 + k4) * h / 6
        x = x + h
        y_mass.append(y)
        x_mass.append(x)
    return y_mass, x_mass


# Метод Адамса-Бэшфорта 3-го порядка
def AB_3_step(mass_y, mass_x, f, h):
    return mass_y[-1] + h * (23 / 12 * f(mass_y[-1], mass_x[-1]) -
                             4 / 3 * f(mass_y[-2], mass_x[-2]) +
                             5 / 12 * f(mass_y[-3], mass_x[-3]))


# Метод Адамса-Бэшфорта 4-го порядка
def AB_4_step(mass_y, mass_x, f, h):
    return mass_y[-1] + h * (55 / 24 * f(mass_y[-1], mass_x[-1]) -
                             59 / 24 * f(mass_y[-2], mass_x[-2]) +
                             37 / 24 * f(mass_y[-3], mass_x[-3]) -
                             3 / 8 * f(mass_y[-4], mass_x[-4]))


# Метод Адамса-Бэшфорта 5-го порядка
def AB_5_step(mass_y, mass_x, f, h):
    return mass_y[-1] + h * (1901 / 720 * f(mass_y[-1], mass_x[-1]) -
                             1387 / 360 * f(mass_y[-2], mass_x[-2]) +
                             109 / 30 * f(mass_y[-3], mass_x[-3]) -
                             637 / 360 * f(mass_y[-4], mass_x[-4]) +
                             251 / 720 * f(mass_y[-5], mass_x[-5]))


# Дифф. уравнение температуры от времени 24-й задачи
def dif_24(T, t):
    k = math.log(3) / 10
    return -k * (T - 25)


# Дифф. уравнение температуры от времени 25-й задачи
def dif_25(T, t):
    return t ** 2 / (2100000 * (0.92 + 0.004 * T))


# Дифф. уравнение давления от высоты 26-й задачи
def dif_26(p, h):
    k = 0.000012
    g = 9.8
    return -k * p * g


# Дифф. уравнение высоты воды от времени 27-й задачи
def dif_27_1(h, t):
    return -0.000248 * (5 * h) ** (1 / 2) / math.pi


def dif_27_2(h, t):
    return -0.0000248 * (5 / (2 - h)) ** (1 / 2)


# Дифф. уравнение высоты воды от времени 28-й задачи
def dif_28(h, t):
    return -1.53 * 10 ** (-5) * 5 ** (1 / 2) * h ** (-3 / 2) / 0.1296
