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

def prime_cube_pairs(n):
    prms = set(sieve(n + 1))
    incr = 6
    test = 1
    total = 0
    while test <= n:
        if test in prms:
            total += 1
        test += incr
        incr += 6
    return total

N = 10 ** 6
print(prime_cube_pairs(N))