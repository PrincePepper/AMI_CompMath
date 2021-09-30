import math

# import matplotlib.pyplot as plt

# xi = a + ih;i = 0, 1, 2, . . . , 10; h = (b − a)/10

# № | y=f(x)    |   [a,b]  | x*   | x**  | x*** | x****|
# 19| y=x2+lg(x)| [0.4,0.9]| 0.53 | 0.43 | 0.86 | 0.67 |
a = 0.4
b = 0.9
h = (b - a) / 10
x_1 = 0.53

mass_x = []
for i in range(1, 11):
    mass_x.append(a + i * h)
print(*mass_x)


def my_func(x):
    return x ** 2 + math.log10(x)


def my_func_derivative_2(x):
    return 2 - 1 / x ** 2 * math.log(10)


def my_func_derivative_3(x):
    return 1 / x ** 3 * math.log(10)


x_i = sorted(mass_x, key=lambda x: abs(x_1 - x))[0]
x_i_1 = sorted(mass_x, key=lambda x: abs(x_1 - x))[1]
x_i_2 = sorted(mass_x, key=lambda x: abs(x_1 - x))[2]
print("xi:", x_i, " ", "xi+1:", " ", x_i_1, "xi-1:", x_i_2)
# L1(x*) = f(xi) · (x* − xi+1)/(xi − xi+1) + f(xi+1) · (x* − xi)/(xi+1 − xi).
L1 = my_func(x_i) * (x_1 - x_i_1) / (x_i - x_i_1) + my_func(x_i_1) * (x_1 - x_i) / (x_i_1 - x_i)
print("L_1(x*): ", L1)

# ω2(x) = (x−xi)·(x−xi+1)
w = (x_1 - x_i) * (x_1 - x_i_1)
print("ω2(x): ", w)

deriv_1 = my_func_derivative_2(x_i)
deriv_2 = my_func_derivative_2(x_i_1)
print('f′′(xi): ', deriv_1, " ", "f′′(x_i+1): ", deriv_2)

R1 = my_func_derivative_2(x_i) * w / 2
R2 = my_func_derivative_2(x_i_1) * w / 2
Rmin = min(R1, R2)
Rmax = max(R1, R2)
print("R_max: ", Rmax, " ", "R_min: ", Rmin)

Rx = my_func_derivative_2(x_1) * w / 2

print("min R1 < R1(x*) < max R1: ", "YES" if (Rmin < Rx < Rmax) else "NO")
print("R1(x*) = L1(x*) − f(x*):", "YES" if (abs(Rx - (L1 - my_func(x_1))) <= 0.01) else "NO")
# print(Rx, L1, my_func(x_1))

L2 = my_func(x_i_2) * (x_1 - x_i) * (x_1 - x_i_1) / (x_i_2 - x_i) / (x_i_2 - x_i_1) + my_func(x_i) * (x_1 - x_i_2) * (
        x_1 - x_i_1) / (
             x_i - x_i_2) / (x_i - x_i_1) + my_func(x_i_1) * (x_1 - x_i) * (x_1 - x_i_2) / (x_i_1 - x_i_2) / (
             x_i_1 - x_i)
print(L2)

# ω3(x) =  (x−xi−1)(x−xi)(x−xi+1)
w3 = (x_1 - x_i_2) * (x_1 - x_i) * (x_1 - x_i_1)
print("ω3(x): ", w3)
R3 = my_func_derivative_3(x_i_1) * w3 / 6
R4 = my_func_derivative_3(x_i_2) * w3 / 6
R2x = my_func_derivative_3(x_1) * w3 / 6
print("R2x: ", R2x)
R2min = min(R3, R4)
R2max = max(R3, R4)
print("R2_max: ", Rmax, " ", "R2_min: ", Rmin)

print("min R2 < R2(x*) < max R2: ", "YES" if (R2min < R2x < R2max) else "NO")
print("R1(x*) = L2(x*) − f(x*):", "YES" if (abs(R2x - (L2 - my_func(x_1))) <= 0.01) else "NO")
