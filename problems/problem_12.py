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
        return 1 + num_factors(n/k, k)[0], num_factors(n/k, k)[1]
    return 0, n

def factorization(n, lst=None):
    facts = {}
    nsmall = math.floor(math.sqrt(n)) + 1
    if lst == None:
        lst = sieve(nsmall)
    i = 0
    while i < len(lst) and lst[i] < nsmall:
        exp, n = num_factors(n, lst[i])
        if exp > 0:
            facts[lst[i]] = exp
        i += 1
    if n != 1:
        facts[n] = 1
    return facts

def triangle_divisors(n, lst):
    divs = {}
    x, y = factorization(n, lst), factorization(n+1, lst)
    for key in x:
        divs[key] = x[key]
    for key in y:
        if key in divs:
            divs[key] += y[key]
        else:
            divs[key] = y[key]
    divs[2] -= 1
    total = 1
    for key in divs:
        total *= (divs[key] + 1)
    return total

def highly_divisible(n):
    prms = sieve(math.floor(math.sqrt(n)))
    k = 2
    while triangle_divisors(k, prms) < n:
        k += 1
    return int(k * (k + 1) / 2)

N = 500
print(highly_divisible(N))