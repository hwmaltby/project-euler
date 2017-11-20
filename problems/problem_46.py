#Henry Maltby 2017
import math

def sieve(n):
    is_prime = [True] * n
    is_prime[0], is_prime[1] = False, False
    prms = []
    for i in range(2, n):
        if is_prime[i]:
            prms.append(i)
            for j in range(i*i, n, i):
                is_prime[j] = False
    return prms

def try_up_to(n):
    vals = [False] * (n + 1)
    prms = sieve(n + 1)[1:]
    prms_set = set(prms)
    i = 0
    while i < len(prms):
        for j in range(1, math.ceil(math.sqrt((n - prms[i]) / 2)) + 1):
            k = prms[i] + 2 * j * j
            if k <= n:
                vals[k] = True
        i += 1
    i = 3
    while i < n:
        if vals[i] == False and i not in prms_set:
            return i
        i += 2
    return -1

N = 10000
print(try_up_to(N))