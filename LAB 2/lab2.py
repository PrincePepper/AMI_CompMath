import math

# xᵢ = a + ih;i = 0, 1, 2, . . . , 10; h = (b − a)/10

# № | y=f(x)    |   [a,b]  | x*   | x**  | x*** | x****|
# 19| y=x²+lg(x)| [0.4,0.9]| 0.53 | 0.43 | 0.86 | 0.67 |
a = 0.4  # левая граница
b = 0.9  # правая граница
h = (b - a) / 10  # шаг
x_star = 0.53  #


def my_function(x):
    return x ** 2 + math.log10(x)


def my_function_derivative_degree_two(x):
    return 2 - 1 / x ** 2 * math.log(10)


def my_function_derivative_degree_three(x):
    return 1 / x ** 3 * math.log(10)


mass_function_x = []
for i in range(0, 11):
    mass_function_x.append(a + i * h)
print(*mass_function_x)

# ---------------------------------------------------------------------------

x_i = sorted(mass_function_x, key=lambda x: abs(x_star - x))[0]
x_i_next = sorted(mass_function_x, key=lambda x: abs(x_star - x))[1]
x_i_back = sorted(mass_function_x, key=lambda x: abs(x_star - x))[2]
print("xi:", x_i, " ", "xi+1:", " ", x_i_next, "xi-1:", x_i_back)

# ---------------------------------------------------------------------------

# L1(x*) = f(xᵢ) · (x* − xᵢ₊₁)/(xi − xᵢ₊₁) + f(xᵢ₊₁) · (x* − xᵢ)/(xᵢ₊₁ − xᵢ).
L1 = my_function(x_i) * (x_star - x_i_next) / (x_i - x_i_next) + my_function(x_i_next) * (x_star - x_i) / (
        x_i_next - x_i)
print("ответ по формуле Лагранжа первого порядка L_1(x*): ", L1)

# ---------------------------------------------------------------------------
# ω2(x) = (x−xᵢ)·(x−xᵢ₊₁)
w2 = (x_star - x_i) * (x_star - x_i_next)
print("ω2(x): ", w2)

deriv_1 = my_function_derivative_degree_two(x_i)
deriv_2 = my_function_derivative_degree_two(x_i_next)
print('f′′(xi): ', deriv_1, " ", "f′′(x_i+1): ", deriv_2)

R1 = my_function_derivative_degree_two(x_i) * w2 / 2
R2 = my_function_derivative_degree_two(x_i_next) * w2 / 2
Rmin = min(R1, R2)
Rmax = max(R1, R2)
print("R_max: ", Rmax, " ", "R_min: ", Rmin)

Rx = my_function_derivative_degree_two(x_star) * w2 / 2

print("min R1 < R1(x*) < max R1: ", "YES" if (Rmin < Rx < Rmax) else "NO")
print("R1(x*) = L1(x*) − f(x*):", "YES" if (abs(Rx - (L1 - my_function(x_star))) <= 0.01) else "NO")

# ------------------------------------------------------------------

L2 = my_function(x_i_back) * (x_star - x_i) * (x_star - x_i_next) / (x_i_back - x_i) / (
        x_i_back - x_i_next) + my_function(x_i) * (
             x_star - x_i_back) * (
             x_star - x_i_next) / (
             x_i - x_i_back) / (x_i - x_i_next) + my_function(x_i_next) * (x_star - x_i) * (x_star - x_i_back) / (
             x_i_next - x_i_back) / (
             x_i_next - x_i)
print("L_2(x*): ", L2)

# ω3(x) = (x−xᵢ₋₁)(x−xᵢ)(x−xᵢ₊₁)
w3 = (x_star - x_i_back) * (x_star - x_i) * (x_star - x_i_next)
print("ω3(x): ", w3)
R3 = my_function_derivative_degree_three(x_i_next) * w3 / 6
R4 = my_function_derivative_degree_three(x_i_back) * w3 / 6
R2x = my_function_derivative_degree_three(x_star) * w3 / 6
print("R2x: ", R2x)
R2min = min(R3, R4)
R2max = max(R3, R4)
print("R2_max: ", Rmax, " ", "R2_min: ", Rmin)

print("min R2 < R2(x*) < max R2: ", "YES" if (R2min < R2x < R2max) else "NO")
print("R1(x*) = L2(x*) − f(x*):", "YES" if (abs(R2x - (L2 - my_function(x_star))) <= 0.001) else "NO")

# ------------------------------------------------------------------

next = my_function(x_i_next)
now = my_function(x_i)
forward = my_function(x_i_back)

print((next - now) - (now - forward))
f_1 = (now - next) / (x_i - x_i_next)
f_2 = (forward - now) / (x_i_back - x_i)
f_3 = (f_1 - f_2) / (x_i_next - x_i_back)

newton_1 = now + f_1 * (x_star - x_i)
newton_2 = forward + f_2 * (x_star - x_i_back) + f_3 * (x_star - x_i_back) * (x_star - x_i)
print(newton_1, newton_2)
print()
print(L1, L2)
print(newton_1, newton_2)
