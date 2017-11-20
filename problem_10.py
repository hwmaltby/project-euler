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

def sum_of_primes(n):
    return sum(sieve(n))

N = 2000000
print(sum_of_primes(N))