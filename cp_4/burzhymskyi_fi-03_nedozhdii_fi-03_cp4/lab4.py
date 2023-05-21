import numpy as np


def L1(x: int) -> tuple[int, int]:
    size = np.log2(x)
    l: int = ((x >> 6) & 1) ^ ((x >> 4) & 1) ^ ((x >> 1) & 1) ^ (x & 1)
    x_0 = x & 1
    x = (x >> 1) ^ (l << 29)
    return x, x_0

def L2(y: int) -> tuple[int, int]:

    l: int = ((y >> 3) & 1) ^ (y & 1)
    y_0 = y & 1
    y = (y >> 1) ^ (l << 30)
    return y, y_0

def L3(s: int) -> tuple[int, int]:
    l: int = ((s >> 7) & 1) ^ ((s >> 5) & 1) ^ ((s >> 3) & 1) ^ ((s >> 2) & 1) ^ ((s >> 1) & 1) ^ (s & 1)
    s_0 = s & 1
    s = (s >> 1) ^ (l << 31)
    return s, s_0

def generatorJiffy(x: int, y: int, s: int) -> int:
    return (s & x) ^ ((1 ^ s) & y)
