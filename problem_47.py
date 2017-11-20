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
    while i < len(lst) and lst[i] < math.floor(math.sqrt(n)) + 1: #should i change this to nsmall? as is, updates
        exp, n = num_factors(n, lst[i])
        if exp > 0:
            facts[lst[i]] = exp
        if n in lst or n == 1:
            break
        i += 1
    if n != 1: #due to this line, does not technically function as _prime_ factorization
        facts[n] = 1
    return facts

factors = {1: 0}

def count_prime_factors(n, prms):
    if n in factors:
        return factors[n]
    n_sqrt = math.ceil(math.sqrt(n))
    i = 0
    while i < len(prms):
        p = prms[i]
        if p > n_sqrt:
            factors[n] = 1
            return factors[n]
        tup = num_factors(n, p)
        if tup[0] > 0:
            factors[n] = 1 + count_prime_factors(tup[1], prms[i + 1:])
            return factors[n]
        i += 1

def consec_integers(n):
    """
    Returns the first of the first n consecutive integers to each have
    prime factorizations containing n distinct primes.
    """
    k = 1
    while True:
        prms = sieve(10 ** k)
        i = 10 ** (k - 1)
        while i < 10 ** k:
            replace = -1
            for j in range(i, i + n):
                if count_prime_factors(j, prms) < n:
                    replace = j + 1
            if replace == -1:
                return i
            i = replace
        k += 1
    return "there's no break statement, haha"

N = 4
print(consec_integers(N))