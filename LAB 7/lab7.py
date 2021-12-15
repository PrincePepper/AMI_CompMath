import math


# def solve_dir(x):
#     return 2 * x + 1 / (math.log(10) * x)
def solve_dir(x):
    return 2 - 1 / (math.log(10) * x ** 2)


def solve(x):
    return x ** 2 + math.log10(x)


def integrate(x, m_i, m_next, h):
    return ((h / 2) * (solve(x) + solve(x + h))) - ((h ** 3 / 24) * (m_i + m_next))


def div(x, m_i, m_next, h):
    return (m_i + 6 / h * (x - (x + h)) * (
            (solve(x + h) - solve(x)) / h - (m_next - 2 * m_i) / 3) + 6 / h ** 2 * (
                    x - (x + h)) ** 2 * ((m_next + m_i) / 2 - (solve(x + h) - solve(x)) / h))


a = 0.4
b = 0.9
h = (b - a) / 10
first = solve_dir(a)
second = solve_dir(b)
# print(first)
# print(second)

low = [0]
main = [2]
high = [1]
result = [(6 / h) * ((solve(a + h) - solve(a)) / h - first)]

i = a + h
while i < b:
    low.append(1 / 2)
    main.append(2)
    high.append(1 / 2)
    result.append((3 / h) * (((solve(i + h) - solve(i)) - (solve(i) - solve(i - h))) / h))
    i += h

low.append(1)
main.append(2)
high.append(0)
result.append((6 / h) * (second - (solve(b) - solve(b - h)) / h))

print(low)
print(main)
print(high)
print(result)

alpha = [0]
betta = [0]
alpha.append(-high[0] / main[0])
betta.append(result[0] / main[0])

n = 11
i = 1

while i < n:
    alpha.append(-high[i] / (main[i] + low[i] * alpha[i]))
    betta.append((-low[i] * betta[i] + result[i]) / (main[i] + low[i] * alpha[i]))
    i += 1

# print(alpha)
# print(betta)

m = [(-low[n - 1] * betta[n - 1] + result[n - 1]) / (main[n - 1] + low[n - 1] * alpha[n - 1])]
i = n - 1
m_count = 0

while i != 0:
    m.append(alpha[i] * m[m_count] + betta[i])
    i -= 1
    m_count += 1

m.reverse()
# print(M)

i = a
integral = 0
index = 0

while i < b:
    print(solve_dir(i), div(i, m[index], m[index + 1], h))
    index += 1
    i += h
