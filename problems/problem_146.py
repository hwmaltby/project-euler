#Henry Maltby
import time
import math

def sieve(n):
    """Returns a list of all primes <= n."""
    a = [True] * (n + 1)
    a[0] = a[1] = False
    lst = []

    for (i, isprime) in enumerate(a):
        if isprime:
            lst.append(i)
            for n in range(i*i, n + 1, i):
                a[n] = False

    return lst

def smart_exp_mod(n, k, mod):
    """Returns n^k mod mod."""
    ans, tmp = 1, (n % mod)
    while k > 0:
        k, r = divmod(k, 2)
        if r == 1:
            ans = (ans * tmp) % mod
        tmp = (tmp * tmp) % mod
    return ans

def miller_rabin(n):
    """
    Assumes n is a positive integer and is accurate for 
    n < 3,825,123,056,546,413,051.
    """
    prms = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    if n in prms:
        return True
    if n % 2 == 0 or n < 23:
        return False
    k, r = n - 1, 0
    while k % 2 == 0:
        k = k // 2
        r += 1
    assert(2**r * k == n - 1)
    for a in prms:
        x = smart_exp_mod(a, k, n)
        if x == 1 or x == n - 1:
            continue
        go_on = False
        for j in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                go_on = True
                continue
        if not go_on:
            return False
    return True

def investigate(prms):
    """
    Determines the acceptable residues mod various primes for possible values
    of n according to the problem constraints.
    """
    fns = [1, 3, 7, 9, 13, 27]
    f = lambda x: x * x
    good_res = {}
    for p in prms:
        good_res[p] = []
        for i in range(p):
            i2 = f(i)
            good = True
            for c in fns:
                if (i2 + c) % p == 0:
                    good = False
                    break
            if good:
                good_res[p].append(1)
            else:
                good_res[p].append(0)
    return good_res

def solve(n):
    """
    Solves the problem. Uses the fact that n^2 = 0 mod 2, 1 mod 3, and 0 mod 5
    in order to reduce the number of primality tests required. Namely, we can
    test only n that are 0 mod 10 and take for granted that n^2 + c is not
    prime for c = 5, 11, 15, 17, 23, 25, or any even value.
    """
    prms = sieve(1500)
    dct = investigate(prms)
    goods = [1, 3, 7, 9, 13, 27]
    bads = [19, 21]

    total = 0
    for i in range(10, n, 10):
        go_on = True
        for p in dct:
            if dct[p][i % p] == 0:
                if p < i + 6:
                    go_on = False
                break
        if go_on:
            i2 = i * i
            stop = False
            for c in goods:
                if not miller_rabin(i2 + c):
                    stop = True
                    break
            for c in bads:
                if miller_rabin(i2 + c):
                    stop = True
                    break
            if stop:
                continue
            total += i

    return total

start = time.time()
#investigate()
N = 150000000
#sieve(N)
print(solve(N))
print("Elapsed time: {:0.4f}".format(time.time() - start))