#Henry Maltby 2017
import math

#in question is y*(1-x-x^2)=x+3x^2 --> (y+3)x^2+(y+1)x-y=0 --> sqrt(5y^2+14y+1)=n
#re-write as (5y+7)^2-5n^2=44 and observe a^2-5b^2=k family has recurrence
#a_{n+1} = 9a_n + 20b_n ; b_{n+1} = 4a_n + 9b_n w initial a_1, b_1 = 17, 7 and 

def recurr(x, y):
    return 9*x+20*y, 4*x+9*y

tries = [(17, 7), (32, 14), (112, 50), (217, 97), (767, 343), (1487, 665)]
counter = 1
total = 0
for i in range(10):
    for i in range(6):
        x, y = tries[i]
        if x % 5 == 2:
            ans = (x - 7) // 5
            total += ans
            print("#{}: {}".format(counter, ans))
            counter += 1
        tries[i] = recurr(x, y)
print("Answer is {}".format(total))

def is_square(n):
    """Returns true if n is a perfect square."""
    x = n // 2
    while x * x != n:
        prev = x
        x = (x + (n // x)) // 2
        if x == prev:
            return False
    return True

for i in range(1, 10000):
    if is_square(5 * i * i + 14 * i + 1):
        print(5 * i + 7)

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