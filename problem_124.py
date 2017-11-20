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

def radical(n, prms):
    total = 1
    for p in prms:
        if n % p == 0:
            while n % p == 0:
                n = n // p
            total *= p
            if n == 1:
                break
    if n != 1:
        total *= n
    return total

def ordered_radicals(n, k):
    prms = sieve(math.ceil(math.sqrt(n)) + 2)
    nums = [(i, radical(i, prms)) for i in range(1, n + 1)]
    tup1 = lambda x: x[1]
    nums.sort(key=tup1)
    return nums[k - 1][0]

N = 10 ** 5
K = 10 ** 4
print(ordered_radicals(N, K))