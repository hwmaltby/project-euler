#Henry Maltby 2017
import math

def is_square(n):
    """Returns true if n is a perfect square."""
    n_sqrt = int(round(math.sqrt(n)))
    return n_sqrt * n_sqrt == n

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

def minl_dio_soln(d):
    """
    Returns the smallest positive solution x to the Diophantine
    equation x^2 - Dy^2 = 1.
    """
    x, i = (0, 0), 1
    per = cont_frac_prd_sqrt(d)
    while not x[0] * x[0] - d * x[1] * x[1] == 1:
        x = cont_frac(i * per, gen_sqrt_con_frac(d))
        i += 1
    return x[0]

def solve_problem(n):
    """
    Returns the value of D <= nsuch that the Diophantine equation
    x^2 - Dy^2 = 1 has the greatest minimal solution in x.
    """
    sqrs = set([i * i for i in range(math.floor(math.sqrt(n)) + 1)])
    maxl_x, D = 3, 2
    for k in range(2, n + 1):
        if k in sqrs:
            continue
        x = minl_dio_soln(k)
        if x > maxl_x:
            maxl_x, D = x, k
    return D

N = 1000
print(solve_problem(N))
