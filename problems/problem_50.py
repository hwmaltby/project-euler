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

def sum_of_most_primes(n):
    """
    Returns the prime <= n that can be written as the sum of the
    greatest number of consecutive primes. Assume n >= 92951.
    """
    prms = sieve(n)
    prms_set = set(prms)
    prm, num = 92951, 183
    for i in range(len(prms)):
        total, count = 0, 0
        while total < n:
            if i + count >= len(prms):
                total = n
            else:
                total += prms[i + count]
                count += 1
                if count > num and total in prms_set:
                    prm, num = total, count
    return prm

N = 1000000
print(sum_of_most_primes(N))