low = [0, 1, 1, 1]
main = [2, 2, 2, 1]
high = [1, 1, 1, 0]
result = [3, 4, 4, 2]

alpha = [0]
betta = [0]
alpha.append(-high[0] / main[0])
betta.append(result[0] / main[0])

n = 4
i = 1

while i < n:
    alpha.append(-high[i] / (main[i] + low[i] * alpha[i]))
    betta.append((-low[i] * betta[i] + result[i]) / (main[i] + low[i] * alpha[i]))
    i += 1

print(alpha)
print(betta)

x = [(-low[n - 1] * betta[n - 1] + result[n - 1]) / (main[n - 1] + low[n - 1] * alpha[n - 1])]
i = n - 1
x_count = 0

while i != 0:
    x.append(alpha[i] * x[x_count] + betta[i])
    i -= 1
    x_count += 1

x.reverse()
print(x)
