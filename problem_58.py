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

def is_prime(n, prms):
    if n in prms:
        return 1
    for p in prms:
        if n % p == 0:
            return 0
        if p * p > n:
            break
    return 1

def spiral_diagonal(perc):
    """
    Returns the side length of the square
    """
    prms = sieve(100000)
    num_prime, num_seen, i = 0, 1, 1
    while num_prime / num_seen >= perc or num_prime == 0:
        sd = 2 * i
        sq = (sd + 1) * (sd + 1)
        num_prime += is_prime(sq, prms)
        num_prime += is_prime(sq - sd, prms)
        num_prime += is_prime(sq - 2*sd, prms)
        num_prime += is_prime(sq - 3*sd, prms)
        num_seen += 4
        i += 1
    return 2 * i - 1

perc = 0.1
print(spiral_diagonal(perc))