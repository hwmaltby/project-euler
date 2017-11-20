#Henry Maltby 2017
#another math hack... you want as many distinct primes as possible :(
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

def euler_totient(facts):
    total = 1
    for p in facts:
        total *= p**facts[p] - p**(facts[p] - 1)
    return total

N = 1000000
prms = sieve(100)
prod, i = 1, 0
while True:
    next = prod * prms[i]
    if next > N:
        break
    prod = next
    i += 1
print(prod)