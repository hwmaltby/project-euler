#Henry Maltby 2017
import math

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

def smart_exp(n, k):
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
    logs = [math.log(p) for p in prms]
    maxl = math.log(2)
    fctrz = [1]
    while count(fctrz) < n:
        test = logs[len(fctrz)]
        for i in range(len(fctrz)):
            if (fctrz[i] + 1) * logs[i] < test:
                fctrz[i] += 1
                break
        else:
            fctrz.append(1)
    fctrz = [3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]
    print(count(fctrz))
    #while count(fctrz) >= n and fctrz[0] > fctrz[1]:
    #    fctrz[0] -= 1
    #if count(fctrz) < n:
    #    fctrz[0] += 1
    #print(fctrz)
    attempt = 1
    fctrz = fctrz
    for i in range(len(fctrz)):
        attempt *= smart_exp(prms[i], fctrz[i])
    #factorizations = {2: [1]}
    #while True:
    #    attempt = min(next)
    #    next.remove(attempt)
    #    fac = factorizations[attempt]
    #    c = count(fac)
    #    print(c)
    #    if c > n:
    #        break
    #    for i in range(len(prms)):
    #        val = attempt * prms[i]
    #        next.add(val)
    #        factorizations[val] = [x for x in fac]
    #        if i < len(factorizations[val]):
    #            factorizations[val][i] += 1
    #        else:
    #            factorizations[val].append(1)
    #            break
    #print(fac)
    return attempt

N = 4000000
print(lowest_exceeding(N))