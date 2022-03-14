from methods import *

eps = 0.001


def task_24():
    T, t = RK4_step(dif_24, 70, 0, eps, 2)
    while T[-1] >= 30:
        T.append(AB_3_step(T, t, dif_24, eps))
        t.append(t[-1] + eps)
    result = t[-1]
    print('result 24 task =', result - 10)


def task_25():
    T, t = RK4_step(dif_25, 0, 0, eps, 3)
    while t[-1] <= 600:
        T.append(AB_4_step(T, t, dif_25, eps))
        t.append(t[-1] + eps)
    result = T[-1]
    print('result 25 task =', result)


def task_26():
    p, h = RK4_step(dif_26, 101325, 0, eps, 4)
    while h[-1] <= 500:
        p.append(AB_5_step(p, h, dif_26, eps))
        h.append(h[-1] + eps)
    result = p[-1]
    print('result 26 task =', result)


def task_27():
    h, t = RK4_step(dif_27_1, 5, 0, eps, 4)
    while h[-1] >= 0:
        h.append(AB_5_step(h, t, dif_27_1, eps))
        t.append(t[-1] + eps)
    result = t[-1]
    print('first result 27 task =', result)

    h, t = RK4_step(dif_27_2, 1.999999999, 0, eps, 2)
    while h[-1] >= 0:
        h.append(AB_3_step(h, t, dif_27_2, eps))
        t.append(t[-1] + eps)
    result = t[-1]
    print('second result 27 task =', result)


def task_28():
    h, t = RK4_step(dif_28, 0.25, 0, eps, 3)
    while h[-1] > 0:
        h.append(AB_4_step(h, t, dif_28, eps))
        t.append(t[-1] + eps)
    result = t[-1]
    print('result 28 task =', result)


if __name__ == '__main__':
    task_24()
    task_25()
    task_26()
    task_27()
    task_28()
