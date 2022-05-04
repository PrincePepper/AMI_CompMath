import math


def matrix_print(matrix, right_side):
    index = 0
    for i in matrix:
        print(i, right_side[index])
        index += 1
    print('\n')


def bubble_max_row(matrix, right_side, n):
    M = matrix.copy()
    R = right_side.copy()
    elements = []
    if n != len(matrix) - 1:
        for i in range(len(matrix)):
            elements.append(matrix[i][n])
        M[n], M[elements.index(max(elements))] = M[elements.index(max(elements))], M[n]
        R[n], R[elements.index(max(elements))] = R[elements.index(max(elements))], R[n]
    return M, R


def straight_stroke(matrix, right_side, n):
    if n != len(matrix):
        diagonal_el = matrix[n][n]
        right_side[n] = right_side[n] / diagonal_el
        for i in range(len(matrix)):
            matrix[n][i] = matrix[n][i] / diagonal_el

        for i in range(n + 1, len(matrix)):
            mul = -matrix[i][n]
            for j in range(len(matrix[0])):
                matrix[i][j] = matrix[n][j] * mul + matrix[i][j]
            right_side[i] = right_side[n] * mul + right_side[i]

    return matrix, right_side


def back_stroke(matrix, right_side, n):
    if n != len(matrix):
        diagonal_el = matrix[n][n]
        right_side[n] = right_side[n] / diagonal_el

        for i in range(n - 1, -1, -1):
            mul = matrix[i][n]
            for j in range(len(matrix[0]) - 1, -1, -1):
                matrix[i][j] = matrix[i][j] - matrix[n][j] * mul
            right_side[i] = right_side[i] - right_side[n] * mul

    return matrix, right_side


def Gauss(matrix, right_side, n):
    M = matrix
    R = right_side
    N = n

    for i in range(0, N):
        M, R = bubble_max_row(M, R, i)
        M, R = straight_stroke(M, R, i)
    matrix_print(M, R)

    for i in range(N - 1, -1, -1):
        M, R = back_stroke(M, R, i)
    matrix_print(M, R)


def main():
    n = 3
    # matrix = []
    # for i in range(n):
    #     matrix.append([int(j) for j in input().split()])
    # right_side = [int(j) for j in input().split()]
    matrix = [
        [0, 69, -5],
        [1, -1, 3],
        [3, 2, -1]
    ]
    right_side = [-2, 5, 4]
    Gauss(matrix, right_side, n)


if __name__ == '__main__':
    main()
