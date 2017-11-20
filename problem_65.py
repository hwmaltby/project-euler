#Henry Maltby 2017
import math

def sum_digits(n):
    """Returns the sum of the digits of n."""
    sum = 0
    for c in str(n):
        sum += int(c)
    return sum

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

def gen_e():
    """Generates the sequence defining the continued fraction of e."""
    yield 2
    i, k = 0, 2
    while True:
        if i % 3 == 1:
            yield k
            k += 2
        else:
            yield 1
        i += 1

def solve_problem(n):
    """Returns the sum of the digits of the nth convergent of e."""
    return sum_digits(cont_frac(n, gen_e())[0])

print(solve_problem(100))