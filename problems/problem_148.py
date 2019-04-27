#Henry Maltby
import time
import math

def solve(p, n):
    """
    Takes as input an integer p and an integer n. Assumed p is prime. Returns
    the number of values in Pascal's triangle through the nth row that are not
    divisible by p. Does so by means of a recurrence on the number of values
    that are divisible by p. Iterates over the length of n in base 7. Practical
    for very large values of n, up until the time required for multiplication
    becomes prohibitive.
    """
    answer, complete, q = 0, 0, n
    b7_rep, partials = [], []
    while q > 0:
        q, r = divmod(q, p)
        b7_rep.append(r)
    for i in range(len(b7_rep)):
        d = b7_rep[i]
        partials.append(d if i == 0 else partials[i - 1] + d * (7 ** i))
        temp, k = tri_num(7 ** i - 1), max(0, (d + 1) * (7 ** i) - partials[i] - 2)
        answer = tri_num(d) * complete + tri_num(d-1) * temp + \
            d * (temp - tri_num(k)) + (d+1) * answer
        complete = tri_num(6) * temp + tri_num(7) * complete
    return tri_num(n + 1) - answer

def tri_num(n):
    """
    Takes as input an integer n. Returns the nth triangular number.
    """
    if n % 2 == 1:
        return n * ((n + 1) // 2)
    return (n // 2) * (n + 1)

start = time.time()
P, N = 7, 10 ** 9
print(solve(P, N - 1))
print("Elapsed time: {:0.4f}".format(time.time() - start))