# a(i,j)=1/(i+j-1)
import math

import numpy


def firstmatrix(r):
    matrix = []
    for i in range(1, r + 1):
        temp_matrix = []
        for j in range(1, r + 1):
            temp_matrix.append(1 / (i + j - 1))
        matrix.append(temp_matrix)
    return matrix


# a(i,j)=min(i,j)/max(i,j)
def secondmatrix(r):
    matrix = []
    for i in range(1, r + 1):
        temp_matrix = []
        for j in range(1, r + 1):
            temp_matrix.append(min(i, j) / max(i, j))
        matrix.append(temp_matrix)
    return matrix


def thirdmatrix(r):
    c = 10000000000000
    matrix = []
    for i in range(1, r + 1):
        temp_matrix = []
        for j in range(1, r + 1):
            temp_matrix.append(c + math.log2(i * j))
        matrix.append(temp_matrix)
    return matrix


print(firstmatrix(10))
print(secondmatrix(10))
print(thirdmatrix(10))

a = firstmatrix(10)
b = [1] * 10
print(b)
x = numpy.linalg.solve(a, b)

c = numpy.dot(a, x)
porog = b - c
print(porog)

print(numpy.linalg.cond(firstmatrix(10)))
print(numpy.linalg.cond(secondmatrix(10)))
print(numpy.linalg.cond(thirdmatrix(10)))
