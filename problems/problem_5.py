#Henry Maltby 2017
import math

def smallest_product(n):
    prod = 1
    prms = primes(n, [])
    for p in prms:
        k = math.floor(math.log(n, p))
        prod *= int(math.pow(p, k))
    return prod

def primes(n, lst):
    if len(lst) == 0:
        lst = [2]
    i = lst[-1] + 1
    while i < n:
        if rel_prime(i, lst):
            lst.append(i)
        i += 1
    return lst

def rel_prime(n, prms):
    k = int(math.floor(math.sqrt(n) + 1))
    i = in_between(k, prms)
    j = 0
    while j <= i:
        if n % prms[j] == 0:
            return False
        j += 1
    return True

def in_between(i, lst):
    if i in lst:
        return lst.index(i)
    j = 0
    for j in range(len(lst)):
        if i < lst[j]:
            break
        j += 1
    return j

N = 20
print(smallest_product(N))