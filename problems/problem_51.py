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

def replace_digits(n, d1, d2):
    """Replaces all occurrences of digit d1 in n with digit d2."""
    n, d1, d2 = str(n), str(d1), str(d2)
    while d1 in n:
        i = n.index(d1)
        n = n[:i] + d2 + n[i + 1:]
    return int(n)

def prime_digit_replacing(n):
    """
    Returns the smallest prime that is in an n prime value family.
    (See problem description.) Only valid for n <= 8.
    """
    prms = sieve(1000000)
    seen = {}
    for p in prms:
        digits = set([int(c) for c in str(p)])
        for d in digits:
            seen[(p, d)] = False
    prms_set = set(prms)
    for p in prms:
        digits = set([int(c) for c in str(p)])
        for d in digits:
            if seen[(p, d)]:
                continue
            count, i = 10, 0
            while count >= n and i < 10:
                if i == 0 and str(p)[0] == str(d):
                    count -= 1
                elif d != i:
                    q = replace_digits(p, d, i)
                    if q in prms_set:
                        seen[q] = True
                    else:
                        count -= 1
                i += 1
            if count >= n:
                return p
    return "try larger sieve"

N = 8
print(prime_digit_replacing(N))