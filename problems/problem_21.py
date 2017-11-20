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

def sum_proper_divisors(n, prms):
    facts = factorization(n, prms)
    prod = 1
    for p in facts:
        prod *= int(round((p**(facts[p] + 1) - 1) / (p - 1)))
    return prod - n

def amicable_numbers(n):
    """
    Sums all amicable numbers (a number in at least one amicable pair)
    between 1 and n.
    """
    lst = [-1] * n
    amis = set()
    prms = sieve(math.floor(math.sqrt(n)) + 1)
    for i in range(n):
        if lst[i] != -1:
            continue
        s = sum_proper_divisors(i + 1, prms)
        lst[i] = s
        if s == 0:
            i += 1
            continue
        if s < n and s != i + 1:
            if lst[s - 1] == -1:
                lst[s - 1] = sum_proper_divisors(s, prms)
            if lst[s - 1] == i + 1:
                amis.add(i + 1)
                amis.add(s)
    return sum(amis)


N = 10000
print(amicable_numbers(N))





