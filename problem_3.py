#Henry Maltby 2017
import math

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

def remove_prime(n, p):
    if n == p:
        return n
    if n % p == 0:
        return remove_prime(n/p, p)
    return n

#def primes(k):
#    lst = [i for i in range(2, k)]
#    i = 2
#    while i < k:
#        j = i
#        while j < k:
#            if j in lst:
#                lst.remove(j)
#            j += i
#        i = lst[lst.index(i) + 1]

N = 600851475143
K = 100000

prms = primes(K, [])
for p in prms:
    N = remove_prime(N, p)
print(N)
