import numpy as np


def relax_method(A, f, n):
    x_prev = x = np.array([0.0] * n)
    w = 1.2

    for _ in range(100):
        for i in range(n):
            S1 = sum((A[i, j] * x[j] for j in range(i)))
            S2 = sum((A[i, j] * x_prev[j] for j in range(i + 1, n)))
            x[i] = (w * (f[i] - S1 - S2) + (1 - w) * A[i, i] * x_prev[i]) / A[i, i]

        x_prev = x

    return x


def main():
    A = np.matrix([
        [10.9, 1.2, 2.1, 0.9],
        [1.2, 11.2, 1.5, 2.5],
        [2.1, 1.5, 9.8, 1.3],
        [0.9, 2.5, 1.3, 12.1]
    ])
    b = np.array([-7.5, 5.3, 10.3, 24.6])

    n = len(b)

    x = relax_method(A, b, n)
    formated_x = np.squeeze(np.asarray(np.around(x, 4)))

    print('Метод релаксации:')
    print('x = ', formated_x)
    print()
    print('Решение (numpy):')
    print(np.around(np.linalg.solve(A, b), 4))


if __name__ == '__main__':
    main()
