class SLE:
    def __init__(self, matrix: [[]], vector: []):
        self.m = matrix
        self.v = vector
        self.dim = len(self.v)

    def get_answer(self):
        return self.v

    def solve(self):
        for i in range(self.dim - 1):
            self.normalize(i)
            for j in range(i + 1, self.dim):
                self.v[j] -= self.v[i]
                for k in range(i, self.dim):
                    self.m[j][k] -= self.m[i][k]
        self.v[-1] /= self.m[-1][-1]
        self.m[-1][-1] = 1

        for i in range(1, self.dim):
            for j in range(i + 1, self.dim + 1):
                factor = self.m[-j][-i]
                self.v[-j] -= self.v[-i] * factor
                for k in range(i, self.dim + 1):
                    self.m[-j][-k] -= self.m[-i][-k] * factor

        return self.m, self.v

    def normalize(self, start):
        for i in range(start, self.dim):
            div = self.m[i][start]
            self.v[i] /= div
            for j in range(self.dim):
                self.m[i][j] /= div


mat = [
    [5, 69, -5],
    [2, -1, 3],
    [6, 2, -1]
]
vec = [-2, 5, 4]
print(*SLE(mat, vec).solve()[1])
# [1.0, 0.0, 0.0] 0.8528735632183908
# [0.0, 1.0, 0.0] -0.01149425287356319
# [0.0, 0.0, 1.0] 1.0942528735632187

# [1.0, 0.3333333333333333, -0.16666666666666666] 0.6666666666666666
# [0.0, 1.0, -0.06188118811881189] -0.07920792079207921
# [0.0, 0.0, 1.0] 1.0942528735632187