#Henry Maltby 2017
import math

def smart_exp_mod(n, k, mod):
    """Returns n^k mod mod."""
    ans, tmp = 1, (n % mod)
    while k > 0:
        k, r = divmod(k, 2)
        if r == 1:
            ans = (ans * tmp) % mod
        tmp = (tmp * tmp) % mod
    return ans

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

def is_prime(n, prms):
    if n == 1:
        return False
    for p in prms:
        if n % p == 0:
            if n == p:
                return True
            return False
    return True

def num_factors(n, k):
    if n % k == 0:
        return 1 + num_factors(n//k, k)[0], num_factors(n//k, k)[1]
    return 0, n

def factorization(n, lst=None):
    facts = {}
    nsmall = math.ceil(math.sqrt(n)) + 1
    if lst == None:
        lst = sieve(nsmall)
    i = 0
    while i < len(lst) and lst[i] < math.ceil(math.sqrt(n)) + 1: #should i change this to nsmall? as is, updates
        exp, n = num_factors(n, lst[i])
        if exp > 0:
            facts[lst[i]] = exp
        if n in lst or n == 1:
            break
        i += 1
    if n != 1: #due to this line, does not technically function as _prime_ factorization
        facts[n] = 1
    return facts

def is_good(n, prms):
    for p in factorization(n - 1, prms):
        test = (n - 1) // p
        if smart_exp_mod(10, test, n) == 1:
            return False
    return True

def find_answer():
    prms = sieve(1100)
    n = 1000003
    while not (is_good(num_factors(n, 3)[1], prms) and (num_factors(n, 3)[0] == 0 or num_factors(n, 3)[1] % 3 == 2)):
        n += 2
        while not (is_prime(n, prms) or (n % 3 == 0 and is_prime(num_factors(n, 3)[1], prms) and n % 5 != 0)):
            n += 2
    return n

print(find_answer())