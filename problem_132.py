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

def find_prime_factors(n, k):
    prms = sieve(1000000)[3:]
    lst = []
    i = 0
    while len(lst) < k and i < len(prms):
        p = prms[i]
        if smart_exp_mod(10, n, p) == 1:
            lst.append(p)
        i += 1
    return sum(lst)

N = 10 ** 9
K = 40
print(find_prime_factors(N, K))