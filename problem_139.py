#Henry Maltby 2017
import time

def euclidean(a, b):
    if b == 0:
        return a
    return euclidean(b, (a % b))

def pythag_tiles(bound):
    n = 1
    total = 0
    seen = set()
    while 4 * n * n < bound:
        m = n + 1
        while 2 * m * (m + n) < bound:
            if euclidean(m, n) != 1:
                m += 1
                continue
            a, b, c = 2 * m * n, m * m - n * n, m * m + n * n
            if c % abs(a - b) == 0:
                gcd = euclidean(euclidean(a, b), euclidean(b, c))
                a, b, c = a // gcd, b // gcd, c // gcd
                a, b = min(a, b), max(a, b)
                if (a, b, c) not in seen:
                    total += bound // (a + b + c)
                    seen.add((a, b, c))
            m += 1
        n += 1
    return total

start = time.time()
N = 10 ** 8
print(pythag_tiles(N))
print("Elapsed time: {:0.4f}".format(time.time() - start))