#Henry Maltby 2017
import bisect

def find_solns(n):
    total = 0
    for p in range(1, n + 1):
        if (n * (n + p)) % p == 0:
            total += 1
    return total

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

def modified_smart_exp(n, k):
    ans, tmp = 1, n
    while k > 0:
        k, r = divmod(k, 2)
        if r == 1:
            ans *= tmp
        tmp *= tmp
    return ans

def expand(fctrz):
    prod = 1
    for p in fctrz:
        prod *= smart_exp(p, fctrz[p])
    return prod

def count(fctrz):
    prod = 1
    for i in fctrz:
        prod *= (2 * i + 1)
    return (prod + 1) // 2

def lowest_exceeding(n):
    prms = sieve(1000)
    queue = [2]
    factorizations = {2: [1]}
    while True:
        attempt = queue.pop(0)
        fac = factorizations[attempt]
        if count(fac) > n:
            break
        for i in range(len(prms)):
            val = attempt * prms[i]
            bisect.insort(queue, val)
            factorizations[val] = [x for x in fac]
            if i < len(fac):
                factorizations[val][i] += 1
            else:
                factorizations[val].append(1)
                break
    print(fac)
    return attempt

N = 1000
print(lowest_exceeding(N))