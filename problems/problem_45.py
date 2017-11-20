#Henry Maltby 2017
import math

def perfect_square(n):
    n_sqrt = int(round(math.sqrt(n)))
    if n_sqrt * n_sqrt == n:
        return n_sqrt
    return -1

def is_hexa(n):
    k = perfect_square(8 * n + 1)
    return (k != -1) and (k % 4 == 3)

def hexa_penta_tri_nums(n):
    penta, inc = 1, 4
    while n > 0:
        if is_hexa(penta):
            n -= 1
        penta += inc
        inc += 3
    return penta - inc + 3

N = 3
print(hexa_penta_tri_nums(N))