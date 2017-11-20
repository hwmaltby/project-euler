#Henry Maltby 2017
import math

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

def num_factors(n, k):
    if n % k == 0:
        return 1 + num_factors(n//k, k)[0], num_factors(n//k, k)[1]
    return 0, n

def factorization(n, lst=None):
    facts = {}
    nsmall = math.floor(math.sqrt(n)) + 1
    if lst == None:
        lst = sieve(nsmall)
    i = 0
    while i < len(lst) and lst[i] < math.floor(math.sqrt(n)) + 1: #should i change this to nsmall? as is, updates
        exp, n = num_factors(n, lst[i])
        if exp > 0:
            facts[lst[i]] = exp
        if n in lst or n == 1:
            break
        i += 1
    if n != 1: #due to this line, does not technically function as _prime_ factorization
        facts[n] = 1
    return facts

def euler_totient(facts):
    total = 1
    for p in facts:
        total *= p**facts[p] - p**(facts[p] - 1)
    return total

def permute(n):
    """
    Returns an integer whose prime factorization uniquely identifies
    the frequencies of each digit in n.
    """
    prms = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    prod = 1
    for c in str(n):
        prod *= prms[int(c)]
    return prod

def bfs(n):
    prms, prms2 = sieve(n), []
    for p in prms:
        if p % 3 == 2:
            prms2.append(p)
    #print(prms2)
    minl_quo, value = math.inf, -1
    stack = [(1, 1, 0)]
    while stack:
        k, tnt, i = stack.pop(0)
        #print(str(k) + ", " + str(tnt) + ", " + str(i))
        if permute(k) == permute(tnt) and k != 1:
            #print("yes")
            quo = k / tnt
            if quo < minl_quo:
                minl_quo, value = quo, k
        j = 1
        #while (prms2[i] ** j) * k < n:
        while i < len(prms2) and prms2[i] * k < n:
            while (prms2[i] ** j) * k < n:
                stack.append(((prms2[i] ** j) * k, ((prms2[i] ** j) -\
                    (prms2[i] ** (j - 1))) * tnt, i + 1))
                j += 1
            j = 1
            i += 1
    stack = [(3, 2, 0)]
    while stack:
        k, tnt, i = stack.pop(0)
        #print(str(k) + ", " + str(tnt) + ", " + str(i))
        if permute(k) == permute(tnt):
            #print("yes")
            quo = k / tnt
            if quo < minl_quo:
                minl_quo, value = quo, k
        j = 1
        while i < len(prms) and prms[i] * k < n:
            while (prms[i] ** j) * k < n:
                stack.append(((prms[i] ** j) * k, ((prms[i] ** j) -\
                    (prms[i] ** (j - 1))) * tnt, i + 1))
                j += 1
            j = 1
            i += 1
    return value

def first_factor(n, prms):
    for p in prms:
        q, r = divmod(n, p)
        if r == 0:
            return p, q
    return n, n

def permute_hash(n):
    hsh = {i: 0 for i in range(10)}
    for c in str(n):
        hsh[int(c)] += 1
    return hsh

def is_permutation(m, n):
    return permute_hash(m) == permute_hash(n)

def different_approach(n):
    n_sqrt = math.floor(math.sqrt(n) + 1)
    prms = sieve(n)
    tnts = [1] * n
    minl_quo, value = math.inf, -1
    for i in range(3, n):
        p, j = first_factor(i, prms)
        if j % p == 0:
            tnts[i] = tnts[j] * p
        else:
            tnts[i] = tnts[j] * (p - 1)
        if is_permutation(i, tnts[i]) and i != 0:
            quo = i / tnts[i]
            if quo < minl_quo:
                minl_quo, value = quo, i
    return value

#DOES NOT WORK. FIXABLE BUT LAZY
def different_approach2(n):
    #note this does not actually create an array of tnts (it's wrong
    #on squares, for instance), but it should suffice for some here
    n_sqrt = math.floor(math.sqrt(n) + 1)
    prms = sieve(n)
    tnts = [1] * n
    minl_quo, value = math.inf, -1
    for i in range(2, n):
        if tnts[i] == 1:
            tnts[i] = i - 1
            for j in range(2, min(i * i, n // i)):
                tnts[j * i] = tnts[j] * tnts[i]
            if i * i < n:
                tnts[i * i] = i * tnts[i]
        if is_permutation(i, tnts[i]):
            quo = i / tnts[i]
            if quo < minl_quo:
                minl_quo, value = quo, i
    return value

def different_approach3(n):
    #here, i assume it is a product of two primes, which seems like a
    #reasonable assumption, provided that at least one exists. as seen
    #by evaluation of one of the other approaches on n = 1000000, this
    #is indeed the case.
    prms = sieve(n // 1000)
    minl_quo, value = math.inf, -1
    for i in range(len(prms)):
        p = prms[i]
        while i + 1 < len(prms) and prms[i + 1] * p < n:
            N, TNT = prms[i + 1] * p, (prms[i + 1] - 1) * (p - 1)
            if is_permutation(N, TNT):
                quo = N / TNT
                if quo < minl_quo:
                    minl_quo, value = quo, N
            i += 1
    return value

N = 10000000
#783169
print(different_approach3(N))