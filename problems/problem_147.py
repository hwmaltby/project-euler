#Henry Maltby
import time
import math

def solve(m, n):
    """
    .
    """
    m, n = max(m, n), min(m, n)
    total = (m+2) * (m+1) * m * (n+2) * (n+1) * n / 36
    for i in range(1, n + 1):
        k1, k2 = n - i, m - i
        to_add = (1 + k1 + k2) * (4 * i*i*i*i - i*i - 3 * i) / 6 + (k1 * (k1 + 1) + k2 * (k2 + 1)) * (4 * i*i*i - i) / 6
        #print(to_add)
        total += to_add
    return total

start = time.time()
M, N = 47, 43
print(solve(M, N))
print("Elapsed time: {:0.4f}".format(time.time() - start))