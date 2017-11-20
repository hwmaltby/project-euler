#Henry Maltby 2017

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

def digit_condition(n):
    if n == 2:
        return True
    n = str(n)
    if '0' in n or '2' in n or '4' in n or '6' in n or '8' in n:
        return False
    return True

def is_circular_prime(n, prms):
    if digit_condition(n):
        n = str(n)
        for i in range(len(n)):
            if int(n[i:] + n[:i]) not in prms:
                return False
        return True
    return False

def find_circular_primes(n):
    """Returns the number of circular primes less than n."""
    prms = sieve(n)
    total = 0
    #could make more efficient by keeping track of circular primes and
    #automatically counting rotations of each circular prime, rather
    #than rediscovering later (as current program does)
    for p in prms:
        if is_circular_prime(p, prms):
            total += 1
    return total

N = 1000000
print(find_circular_primes(N))