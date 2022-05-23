'''
https://matica.org.ua/metodichki-i-knigi-po-matematike/chislennye-metody-iu-ia-katcman/
3-8-metod-skoreishego-spuska-gradienta-dlia-sluchaia--sistemy-lineinykh-algebraicheskikh-uravnenii
'''

import numpy as np


def check(r):
    for el in r:
        if abs(el) > 10e-8:
            return False
    return True


__N = 4
# problem
a = np.array([
    [8, -1, -2, 0],
    [0, 10, -2, 2],
    [-1, 0, 6, 2],
    [3, -1, 2, 12]
])
x = np.array([0, 0, 0, 0])
b = np.array([2.3, -0.5, -1.2, 3.7])
'''
    x1 = 647 / 3205 = 0.2018720748829953
    x2 = -2053 / 12820 = -0.1601404056162246
    x3 = -6729 / 25640 = -0.2624414976599064
    x4 = 7391 / 25640 = 0.2882605304212168
'''
# solution

k = 0
while True:
    k += 1
    r = (a.dot(x) - b)
    buf = a.dot(a.transpose()).dot(r)
    u = np.dot(buf, r) / np.dot(buf, buf)
    x = x - u * a.transpose().dot(r)

    if check(r):
        break

print(f'k:{k}')
print(x)
