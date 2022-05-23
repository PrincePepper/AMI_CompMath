import numpy as np


def invert(M, depth=0):
    n, k = len(M), len(M) - 1
    if n == 1:
        return np.matrix([[1 / M[0, 0]]])

    v, u = M[k, :k], M[:k, k]
    M_inv = invert(M[:k, :k], depth + 1)
    alpha = (M[k, k] - v * M_inv * u).item()

    A = M_inv + (M_inv * u * v * M_inv) / alpha
    B = - M_inv * u / alpha
    C = - v * M_inv / alpha
    D = 1 / alpha

    Inv = np.zeros((n, n))
    Inv[:k, :k] = A
    Inv[:k, k:] = B[:, 0]
    Inv[k, :k] = C[0]
    Inv[k, k] = D

    return Inv


def main():
    M = np.matrix([
        [81., -45., 45.],
        [-45., 50., -15.],
        [45., -15., 38.]
    ])

    print('Матрица:')
    print(M)
    print()
    print('Инвертированная матрица (numpy):')
    print(np.linalg.inv(M))
    print()
    print('Инвертированная матрица:')
    print(invert(M))


if __name__ == '__main__':
    main()
