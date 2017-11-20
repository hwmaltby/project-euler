#Henry Maltby 2017
import time

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

def euclidean(a, b):
    """Return x and y such that ax+by=gcd(a, b). Require a >= b."""
    if b == 0:
        return 1, 0
    q, r = divmod(a, b)
    tup = euclidean(b, r)
    return tup[1], tup[0] - q * tup[1]

def prime_pair_connection(n):
    prms = sieve(11 * n // 10 + 10)[2:]
    total = 0
    p1 = prms.pop(0)
    p2 = prms.pop(0)
    while p1 <= n:
        mod = 10 ** len(str(p1))
        x, y = euclidean(p2, mod)
        S = ((x * p1) % mod) * p2
        total += S
        p1 = p2
        p2 = prms.pop(0)
    return total

N = 10 ** 6
print(prime_pair_connection(N))