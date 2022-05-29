import numpy as np


def get_max(A):
    max_elem = (1, 0)
    for i in range(A.shape[0]):
        for j in range(i):
        if abs(A[max_elem]) < abs(A[i, j]):
        max_elem = (i, j)
    return max_elem


def rotation(matrix):
    for k in range(15):
        l, m = get_max(matrix)
    angle = np.arctan(2 * matrix[l, m] / (matrix[l, l] - matrix[m, m])) / 2
    T = np.eye(matrix.shape[0])
    T[l, l] = np.cos(angle)
    T[l, m] = -np.sin(angle)
    T[m, l] = np.sin(angle)
    T[m, m] = np.cos(angle)
    matrix = T.T * matrix * T
    return matrix


A = np.matrix([
    [-0.168700, 0.353699, 0.008540, 0.733624],
    [0.353699, 0.056519, 0.723182, -0.076440],
    [0.008540, 0.723182, 0.015938, 0.342333],
    [0.733624, -0.076440, 0.342333, -0.045744]
])
print(rotation(A))
print(np.linalg.eig(A)[0])
