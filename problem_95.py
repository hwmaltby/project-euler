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

def num_factors(n, k):
    if n % k == 0:
        return 1 + num_factors(n//k, k)[0], num_factors(n//k, k)[1]
    return 0, n

def amicable_chains(n):
    prms = sieve(n + 1)
    prms_set = set(prms)
    totient_proper = [0] * (n + 1)
    for i in range(2, n + 1):
        if i in prms_set:
            totient_proper[i] = 1
            new = i * i
            while new < n + 1:
                totient_proper[new] = (new - 1) // (i - 1)
                new *= i
        if totient_proper[i] == 0:
            j = 0
            while prms[j] * prms[j] <= i:
                e, q = num_factors(i, prms[j])
                if e > 0:
                    p = i // q
                    totient_proper[i] = (q + totient_proper[q]) * (p + totient_proper[p]) - i
                j += 1
    unused = [True] * (n + 1)
    unused[0] = False
    best = [0]
    for i in range(n + 1):
        if unused[i]:
            d, path = totient_proper[i], [i]
            while d <= n and d not in path:
                path.append(d)
                d = totient_proper[d]
            if d <= n:
                path = path[path.index(d):]
                if len(path) > len(best):
                    best = path
        unused[i] = False
    return min(best)

N = 1000000
print(amicable_chains(N))