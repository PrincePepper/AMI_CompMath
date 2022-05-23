import numpy as np


def simple_iteration(A, f, n):
    ls = np.linalg.eig(A)[0]
    alpha, beta = min(ls), max(ls)
    k = 2.0 / (alpha + beta)
    x = np.array([0] * n)

    for _ in range(1000):
        x = x - (x * A - f) * k

    return x


def main():
    A = np.matrix([
        [10.9, 1.2, 2.1, 0.9],
        [1.2, 11.2, 1.5, 2.5],
        [2.1, 1.5, 9.8, 1.3],
        [0.9, 2.5, 1.3, 12.1]
    ])
    b = np.array([-7.5, 5.3, 10.3, 24.6])

    n = len(A)

    x = simple_iteration(A, b, n)
    formated_x = np.squeeze(np.asarray(np.round(x, 4)))

    print('x = ', formated_x)


if __name__ == '__main__':
    main()
