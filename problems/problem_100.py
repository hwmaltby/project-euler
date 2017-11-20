#Henry Maltby 2017
import math

def is_square(n):
    """Returns true if n is a perfect square."""
    x = n // 2
    while x * x != n:
        prev = x
        x = (x + (n // x)) // 2
        if x == prev:
            return False
    return True

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

def cont_frac(n, gen):
    """
    Returns the nth convergent of a continued fraction with expansion
    given by the values in gen.
    """
    p0, q0 = 0, 1
    p1, q1 = 1, 0
    while n > 0:
        a = next(gen)
        p1, q1, p0, q0 = a*p1 + p0, a*q1 + q0, p1, q1
        n -= 1
    return (p1, q1)

def cont_frac_prd_sqrt(n):
    """Returns the period of the continued fraction of sqrt(n)."""
    expan = gen_sqrt_con_frac(n)
    a0 = next(expan)
    i = 0
    for x in expan:
        i += 1
        if x == 2 * a0:
            return i

def find_dio_solns(d, n):
    """
    Returns all values x <= n that yield an integer solution (x, y) to
    the Diophantine equation x^2 - Dy^2 = -1.
    """
    solns = []
    x, i = (0, 0), 0
    while x[0] <= n:
        #per = cont_frac_prd_sqrt(d)
        if x[0] * x[0] - d * x[1] * x[1] == -1 and (x[0] != 1 or 1 not in solns):
            solns.append(x)
        x = cont_frac(i, gen_sqrt_con_frac(d))
        i += 1
    return solns

def arranged(n):
    lst = find_dio_solns(2, 10 * n)
    maxl = -1
    while (lst[-1][0] + 1) // 2 > n:
        maxl = (lst.pop()[1] + 1) // 2
    return maxl

N = 10 ** 12
print(arranged(N))