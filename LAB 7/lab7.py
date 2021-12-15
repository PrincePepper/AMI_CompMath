import math

import matplotlib.pyplot as plt


def solve_dir(x):
    return 2 - 1 / (math.log(10) * x ** 2)


def solve(x):
    return x ** 2 + math.log10(x)


def integrate(x, m_i, m_next, h):
    return ((h / 2) * (solve(x) + solve(x + h))) - ((h ** 3 / 24) * (m_i + m_next))


def div(x, m_i, m_next, h):
    return (m_i + 6 / h * (x - (x + h)) * (
            (solve(x + h) - solve(x)) / h - (m_next - 2 * m_i) / 3) + 6 / h ** 2 * (
                    x - (x + h)) ** 2 * ((m_next + m_i) / 2 - (solve(x + h) - solve(x)) / h))


a = 0.4
b = 0.9
n = 11
h = (b - a) / 10
segment = [a + h * i for i in range(11)]
gov = [solve(i) for i in segment]

# нижняя диагональ
diag_1i = [0.5 if i != 9 else 1 for i in range(11 - 1)]
diag_1i.insert(0, 0)

# главная диагональ
diag_i = [2 for _ in range(11)]

# верхняя диагональ
diag_i1 = [0.5 if i != 0 else 1 for i in range(11 - 1)]
diag_i1.append(0)

# вектор правой части
resuilt = []
for i in range(11):
    if i == 0:
        resuilt.append((3 / h) * (gov[i + 1] - gov[i]) - (h / 2) * solve_dir(segment[i]))
    elif i == 10:
        resuilt.append((h * solve_dir(segment[i]) / 2) + 3 * ((gov[i] - gov[i - 1]) / h))
    else:
        resuilt.append(30 * (gov[i + 1] - gov[i - 1]))


def solveMatrix(n, a, c, b, f):
    m = 0
    x = [0 for i in range(n)]
    for i in range(1, n):
        m = a[i] / c[i - 1]
        c[i] = c[i] - m * b[i - 1]
        f[i] = f[i] - m * f[i - 1]

    x[n - 1] = f[n - 1] / c[n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = (f[i] - b[i] * x[i + 1]) / c[i]

    return x


# пример
mi = solveMatrix(11, diag_1i, diag_i, diag_i1, resuilt)


def S(x, i):
    res = 0
    a1 = 6 / h
    a2 = (gov[i + 1] - gov[i]) / h
    a3 = (mi[i + 1] + 2 * mi[i]) / 3
    a4 = 12 * (x - segment[i]) / (h ** 2)
    a5 = (mi[i + 1] + mi[i]) / 2
    a6 = (gov[i + 1] - gov[i]) / h
    res += a1 * (a2 - a3) + a4 * (a5 - a6)
    return res


govS2 = []
for j, i in enumerate(segment):
    if j == 10:
        j = 9
    govS2.append(S(i, j))
# govS2 = [S2(i, j-1) for j, i in enumerate(segment)]
govy2 = [solve_dir(i) for i in segment]

plt.plot(segment, govy2)
plt.plot(segment, govS2)
plt.legend(['Функция', 'Сплайн'], loc=2)
plt.show()
