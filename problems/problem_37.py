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

def is_truncatable_prime(n, prms):
    if n > 100 and not digit_condition(n):
        return False
    for i in range(len(str(n))):
        k = n // (10 ** i)
        if k not in prms:
            return False
        if n - k * (10 ** i) not in prms and i != 0:
            return False
    return True

def sum_all_truncatable_primes():
    prms = set(sieve(1000000))
    total = 0
    for p in prms:
        if is_truncatable_prime(p, prms) and p > 10:
            total += p
    return total

print(sum_all_truncatable_primes())