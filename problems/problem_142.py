#Henry Maltby 2017
import time
import math
import numpy as np

def gen_prim_pyth_trips(limit=None):
    """Generates all primitive Pythagorean triplets using UAD decomposition.
    Credit to StackExchange."""
    u = np.mat(' 1  2  2; -2 -1 -2; 2 2 3')
    a = np.mat(' 1  2  2;  2  1  2; 2 2 3')
    d = np.mat('-1 -2 -2;  2  1  2; 2 2 3')
    uad = np.array([u, a, d])
    m = np.array([3, 4, 5])
    while m.size:
        m = m.reshape(-1, 3)
        if limit:
            m = m[m[:, 2] <= limit]
        yield from m
        m = np.dot(m, uad)

def gen_all_pyth_trips(limit):
    """Generates all Pythagorean triplets up to a certain limit."""
    for prim in gen_prim_pyth_trips(limit):
        i = prim
        for _ in range(limit // prim[2]):
            yield i
            i = i + prim

def is_square(n):
    """Returns true if n is a perfect square."""
    if n == 0 or n == 1:
        return True
    x = n // 2
    prev = n
    while x * x != n:
        prev2 = prev
        prev = x
        x = (x + (n // x)) // 2
        if x == prev or x == prev2:
            return False
    return True

def check_solution(x, y, z):
    """Returns true if x, y, z satisfy the problem conditions."""
    return x > y and y > z and z > 0 and is_square(y - z) and is_square(x - z) \
        and is_square(x - y) and is_square(x + y) and is_square(x + z) \
        and is_square(y + z)

def solve(N):
    """Searches for an answer to the problem bounded (in some way) by N."""
    trips = list(gen_all_pyth_trips(N))
    hyps = {}

    for x, y, z in trips:
        if z in hyps:
            hyps[z].add((x, y))
        else:
            hyps[z] = {(x, y)}

    smallest = math.inf
    for a, b, c in trips:
        for _ in range(2):
            a, b = b, a
            if a in hyps:
                for tup in hyps[a]:
                    #print(tup)
                    u, v = tup
                    for _ in range(2):
                        u, v = v, u
                        x = u * u + c * c
                        if x % 2 != 0:
                            continue
                        x = x // 2
                        y = x - u * u
                        z = v * v - y
                        if check_solution(x, y, z):
                            tmp = x + y + z
                            if tmp < smallest:
                                smallest = tmp
                                print("{}, {}, {}".format(x, y, z))
    return smallest


start = time.time()
N = 10 ** 4
print(solve(N))
print("Elapsed time: {:0.4f}".format(time.time() - start))