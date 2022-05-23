import numpy as np


def qr_factorization(A, n):
    Q = np.empty((n, n))
    u = np.empty((n, n))

    u[:, 0] = A[:, 0]
    Q[:, 0] = u[:, 0] / np.linalg.norm(u[:, 0])

    for i in range(1, n):
        u[:, i] = A[:, i]

        for j in range(i):
            u[:, i] -= (A[:, i] @ Q[:, j]) * Q[:, j]

        Q[:, i] = u[:, i] / np.linalg.norm(u[:, i])

    R = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            R[i, j] = A[:, j] @ Q[:, i]

    return Q, R


def find_eigvals(A, n, eps=1e-10):
    A_old = A_new = np.copy(A)
    diff, i = np.inf, 0

    while (diff > eps) and (i < 1000):
        A_old[:, :] = A_new
        Q, R = qr_factorization(A_old, n)

        A_new[:, :] = R @ Q

        diff = np.abs(A_new - A_old).max()
        i += 1

    return np.diag(A_new)


def main():
    A = np.array([[1., 2., 4.],
                  [3., 3., 2.],
                  [4., 1., 3.]])

    n = A.shape[0]

    Q, R = qr_factorization(A, n)
    eigvals = find_eigvals(A, n)

    print('Q:')
    print(Q)
    print('R:')
    print(R)
    print('Собственные значения:')
    print(eigvals)


if __name__ == '__main__':
    main()
