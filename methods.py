import ctypes
import math
from functools import lru_cache
from typing import List
from tabulate import tabulate


def check_equidistant_nodes(nodes):
    h = nodes[1] - nodes[0]
    for i in range(len(nodes) - 1):
        if not math.isclose(nodes[i + 1] - nodes[i], h):
            return False
    return True


@lru_cache
def get_dy(id_y: int, len_y: int) -> List[List[float]]:
    y = ctypes.cast(id_y, ctypes.py_object).value
    dy = [[i] for i in y]
    for i in range(1, len(y)):
        for j in range(len(y) - i):
            dy[j].append(dy[j + 1][-1] - dy[j][-1])
    field_names = ['yi'] + [f'd{i} Yi' for i in range(1, len(dy))]
    print("\n" + tabulate(dy, field_names, tablefmt='grid', floatfmt='2.4f') + "\n")
    return dy


def calc_t_stuff(k: int, t: float) -> float:
    if k == 0:
        return 1
    else:
        t_mul = 1
        for i in range(k):
            t_mul *= (t - i)
        return t_mul / math.factorial(k)


def newton(x: List[float], y: List[float], x0: float):
    if not check_equidistant_nodes(x):
        raise Exception('Узлы не являются равноотстоящими, метод Ньютона с конечными разностями не применим.')

    dy = get_dy(id(y), len(y))
    t = (x0 - x[0]) / (x[1] - x[0])
    result = 0
    for i in range(len(x)):
        result += dy[0][i] * calc_t_stuff(i, t)
    return result


def lagrange(x: List[float], y: List[float], x0: float):
    result = 0
    for j in range(len(y)):
        mul = 1
        for i in range(len(x)):
            mul *= (x0 - x[i]) / (x[j] - x[i]) if i != j else 1
        result += y[j] * mul
    return result
