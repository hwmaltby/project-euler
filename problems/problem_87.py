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

def sum_of_prime_powers(n):
    """
    Returns the amount of numbers less than n that are the sum of a
    prime squared, a prime cubed, and a prime raised to the fourth
    power.
    """
    prms = sieve(math.floor(math.sqrt(n)) + 1)
    r = len(prms)
    cool_nums = set()
    for i in range(r):
        j = 0
        while prms[i] ** 2 + prms[j] ** 3 < n:
            k = 0
            while prms[i] ** 2 + prms[j] ** 3 + prms[k] ** 4 < n:
                cool_nums.add(prms[i] ** 2 + prms[j] ** 3 + prms[k] ** 4)
                k += 1
            j += 1
    return len(cool_nums)

N = 50000000
print(sum_of_prime_powers(N))