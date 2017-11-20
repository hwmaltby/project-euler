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

def check_primes(a, b, prms):
    """
    """
    n = 3
    while (n * n + a * n + b) in prms:
        n += 1
    return n - 1

def quadratic_primes(n):
    """
    Returns the product a * b of integers a, b: |a|, |b| < n; such
    that the polynomial x^2 + a*x + b yields prime values for the
    maximal consecutive positive integers x, among all possible a, b.
    For certain values of n, sieve may not be large enough.
    """
    prms = set(sieve(max(10 * n, 10000)))
    a_max, b_max, m_max = 0, 0, 0
    for p in prms:
        for a in range(-n + 1, n):
            b = p - a - 1
            if abs(b) < n and (4 + 2 * a + b) in prms:
                m = check_primes(a, b, prms)
                if m > m_max:
                    a_max, b_max, m_max = a, b, m
    return a_max * b_max

N = 1000
print(quadratic_primes(N))