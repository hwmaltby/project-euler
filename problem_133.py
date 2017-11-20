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

def smart_exp_mod(n, k, mod):
    """Returns n^k mod mod."""
    ans, tmp = 1, (n % mod)
    while k > 0:
        k, r = divmod(k, 2)
        if r == 1:
            ans = (ans * tmp) % mod
        tmp = (tmp * tmp) % mod
    return ans

def num_factors(n, k):
    if n % k == 0:
        return 1 + num_factors(n//k, k)[0], num_factors(n//k, k)[1]
    return 0, n

def strip_factors(n, prms):
    total = 1
    for p in prms:
        e, n = num_factors(n, p)
        total *= p ** e
    return total

def find_prime_factors(n):
    prms = sieve(n)[3:]
    lst = []
    for p in prms:
        if smart_exp_mod(10, strip_factors(p - 1, [2, 5]), p) == 1:
            lst.append(p)
    return sum(prms) - sum(lst) + 10

N = 10 ** 5
print(find_prime_factors(N))