#Henry Maltby 2017
import math

def gen_sqrt_con_frac(n):
    """
    Generates the sequence defining the continued fraction of sqrt(n).
    If n is a perfect square, throws error.
    """
    n_sqrt = math.sqrt(n)
    a, b = math.floor(math.sqrt(n)), 1
    c = - a
    while True:
        yield a
        b = (n - c * c) / b
        a = math.floor((math.sqrt(n) - c) / b)
        c = - c - a*b

def cont_frac_prd_sqrt(n):
    """Returns the period of the continued fraction of sqrt(n)."""
    expan = gen_sqrt_con_frac(n)
    a0 = next(expan)
    i = 0
    for x in expan:
        i += 1
        if x == 2 * a0:
            return i

def odd_prd_sqrts(n):
    """
    Returns the amount of positive integers k <= n such that the
    continued fraction of sqrt(n) has odd period.
    """
    sqrs = set([i * i for i in range(math.floor(math.sqrt(n)) + 1)])
    total = 0
    for k in range(2, n + 1):
        if k in sqrs:
            continue
        if cont_frac_prd_sqrt(k) % 2 == 1:
            total += 1
    return total

N = 10000
print(odd_prd_sqrts(N))