import numpy as np


def jacobi(A, f, n):
    x_prev = x = np.array([0.0] * n)

    for _ in range(100):
        for i in range(n):
            S = sum([A[i, j] * x_prev[j] if i != j else 0 for j in range(n)])
            x[i] = (f[i] - S) / A[i, i]

        x_prev = x

    return x


def seidel(A, f, n):
    x_prev = x = np.array([0.0] * n)

    for _ in range(100):
        for i in range(n):
            S1 = sum((A[i, j] * x[j] for j in range(i)))
            S2 = sum((A[i, j] * x_prev[j] for j in range(i + 1, n)))
            x[i] = (f[i] - S1 - S2) / A[i, i]

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

    x_jacobi = jacobi(A, b, n)
    x_seidel = seidel(A, b, n)
    formated_x_jacobi = np.squeeze(np.asarray(np.around(x_jacobi, 4)))
    formated_x_seidel = np.squeeze(np.asarray(np.around(x_seidel, 4)))

    print('Метод Якоби:')
    print('x = ', formated_x_jacobi)
    print()
    print('Метод Зейделя:')
    print('x = ', formated_x_seidel)
    print()
    print('Решение (numpy):')
    print(np.linalg.solve(A, b))


if __name__ == '__main__':
    main()
