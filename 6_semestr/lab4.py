import numpy

import numpy as np


# решение СЛАУ Метод Гаусса с выбором главного элемента, обработка нуля на диагонали.
class SLE:
    def __init__(self, matrix: [[]], vector: []):
        self.m = matrix
        self.m = numpy.array(self.m, dtype=float)
        self.v = vector
        self.v = numpy.array(self.v, dtype=float)
        self.dim = len(self.v)

        self.m_lu = [[]]
        self.res = self.generalGauss(self.m, self.v)

    def makeIdentity(self, matrix):
        # перебор строк в обратном порядке
        for nrow in range(len(matrix) - 1, 0, -1):
            row = matrix[nrow]
            for upper_row in matrix[:nrow]:
                factor = upper_row[nrow]
                # вычитать строки не нужно, так как в row только два элемента отличны от 0:
                # в последней колонке и на диагонали

                # вычитание в последней колонке
                upper_row[-1] -= factor * row[-1]
                # вместо вычитания 1*factor просто обнулим коэффициент в соотвествующей колонке.
                upper_row[nrow] = 0
        return matrix

    def makeTrianglePivot(self, matrix):
        for nrow in range(len(matrix)):
            # nrow равен номеру строки
            # np.argmax возвращает номер строки с максимальным элементом в уменьшенной матрице
            # которая начинается со строки nrow. Поэтому нужно прибавить nrow к результату
            pivot = nrow + np.argmax(abs(matrix[nrow:, nrow]))
            if pivot != nrow:
                # swap
                # matrix[nrow], matrix[pivot] = matrix[pivot], matrix[nrow] - не работает.
                # нужно переставлять строки именно так, как написано ниже
                # matrix[[nrow, pivot]] = matrix[[pivot, nrow]]
                matrix[nrow], matrix[pivot] = matrix[pivot], np.copy(matrix[nrow])
            row = matrix[nrow]
            divider = row[nrow]  # диагональный элемент
            if abs(divider) < 1e-10:
                # почти нуль на диагонали. Продолжать не имеет смысла, результат счёта неустойчив
                raise ValueError("Матрица несовместна")
            # делим на диагональный элемент.
            row /= divider
            # теперь надо вычесть приведённую строку из всех нижележащих строчек
            for lower_row in matrix[nrow + 1:]:
                factor = lower_row[nrow]  # элемент строки в колонке nrow
                lower_row -= factor * row  # вычитаем, чтобы получить ноль в колонке nrow
        return matrix

    def gaussSolvePivot(self, A, b=None):
        """Решает систему линейных алгебраических уравнений Ax=b
        Если b is None, то свободные коэффициенты в последней колонке"""
        shape = A.shape
        assert len(shape) == 2, ("Матрица не двумерная", shape)  # двумерная матрица
        A = A.copy()
        if b is not None:
            assert shape[0] == shape[1], ("Матрица не квадратная", shape)
            assert b.shape == (shape[0],), (
                "Размерность свободных членов не соответствует матрица", shape, b.shape)
            # добавляем свободные члены дополнительным столбцом
            A = np.c_[A, b]
        else:
            # Проверяем, что квадратная плюс столбец
            assert shape[0] + 1 == shape[1], ("Неверный формат матрицы", shape)
        self.makeTrianglePivot(A)
        self.makeIdentity(A)
        return A[:, -1]

    def generalGauss(self, A, b):
        """Решает систему линейных алгебраических уравнений Ax=b
        Если b is None, то свободные коэффициенты в последней колонке"""
        shape = A.shape
        assert len(shape) == 2, ("Матрица не двумерная", shape)  # двумерная матрица
        A = A.copy()
        if b is not None:
            assert shape[0] == shape[1], ("Матрица не квадратная", shape)
            assert b.shape == (shape[0],), (
                "Размерность свободных членов не соответствует матрица", shape, b.shape)
            # добавляем свободные члены дополнительным столбцом
            A = np.c_[A, b]
        else:
            # Проверяем, что квадратная плюс столбец
            assert shape[0] + 1 == shape[1], ("Неверный формат матрицы", shape)
        A = self.makeTrianglePivot(A)
        self.m_lu = A.copy()
        A = self.makeIdentity(A)
        return np.array([r[-1] for r in A])

    def result(self):
        return self.res

    def get_mat(self):
        return self.m

    def get_vec(self):
        return self.v

    def get_L_m(self):
        return self.m_lu


def LU_decomposition(matrix: [[]]):  # L'U' = A' - vw^t / a_11
    n = len(matrix)
    U = []
    L = []
    for i in range(n):
        U.append([])
        L.append([])
        for j in range(n):
            U[i].append(0)
            L[i].append(0)

    for i in range(n):
        L[i][i] = 1

    for i in range(n):
        for j in range(n):
            if i <= j:
                sub = 0
                for k in range(i):
                    sub += L[i][k] * U[k][j]
                U[i][j] = matrix[i][j] - sub
            else:
                sub = 0
                for k in range(j):
                    sub += L[i][k] * U[k][j] / U[j][j]
                L[i][j] = matrix[i][j] - sub

    return L, U


def solve_LU(L: [[]], U: [[]], b: []):
    sle = SLE(L, b)
    sle = SLE(U, sle.result())
    return sle.result()


def square_decomp(a: [[]]):
    n = len(a)
    t = []
    for i in range(n):
        t.append([])
        for j in range(n):
            t[i].append(0)

    for i in range(n):
        for j in range(n):
            if i == j == 0:
                t[i][j] = a[i][j] ** (1 / 2)
            elif i == 0 and j > 0:
                t[i][j] = a[i][j] / t[0][0]
            elif i == j and i > 0:
                sub = 0
                for k in range(i):
                    sub += t[k][i] ** 2
                t[i][j] = (a[i][j] - sub) ** (1 / 2)
            elif i < j:
                sub = 0
                for k in range(i):
                    sub += t[k][i] * t[k][j]
                t[i][j] = (a[i][j] - sub) / t[i][i]
            else:
                t[i][j] = 0
    return t


def main():
    matrix = [
        [1, 2, 4],
        [2, 0, 23],
        [4, 23, 0]
    ]
    vec = [10, 50, 150]

    # print(SLE(matrix, vec).result())
    # print(*SLE2(matrix, vec).solve()[1])
    #
    # L, U = LU_decomposition(matrix)
    # print(solve_LU(L, U, vec))
    # print(solve_LU2(L, U, vec))

    T = square_decomp(matrix)
    print(solve_LU(numpy.transpose(T), T, vec))


if __name__ == '__main__':
    main()
