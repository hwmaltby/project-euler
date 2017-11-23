#Henry Maltby 2017
import math
import time
#please come back and make a faster time, currently is ridiculously bad
#going back to pre-computed radicals will make it reasonable
#and going by a sorted list of those should make it good

def sieve(n):
    a = [True] * (n + 1)
    a[0] = a[1] = False
    lst = []

    for (i, isprime) in enumerate(a):
        if isprime:
            lst.append(i)
            for n in range(i*i, n + 1, 2*i):
                a[n] = False

    return lst

def squarefree(n):
    sqfr = [True] * (n + 1)
    fctrs = [set() for _ in range(n + 1)]
    prms = sieve(math.floor(math.sqrt(n) + 1))
    for i in range(2, n + 1):
        for p in prms:
            if p * p > i:
                break
            q, r = divmod(i, p)
            if r == 0:
                if q % p == 0:
                    sqfr[i] = False
                    fctrs[i] = fctrs[q].copy()
                else:
                    sqfr[i] = sqfr[q]
                    fctrs[i] = fctrs[q].copy()
                    fctrs[i].add(p)
                break
        if len(fctrs[i]) == 0:
            fctrs[i].add(i)
    return sqfr, fctrs

def mult_set(s):
    total = 1
    for x in s:
        total *= x
    return total

def find_abcs(n):
    sqfr, fctrs = squarefree(n)
    evens = []
    odds = []

    for i in range(8, n + 1):
        if not sqfr[i]:
            if i % 2 == 0:
                evens.append(i)
            else:
                odds.append(i)

    abcs = []

    for i in evens:
        print(i)
        for j in odds:
            if j > 2 * i:
                break
            if i >= 2 * j:
                continue
            if fctrs[i] - fctrs[j] != fctrs[i]:
                continue
            b, c = min(i, j), max(i, j)
            a = c - b
            if mult_set(fctrs[a]) * mult_set(fctrs[b]) * mult_set(fctrs[c]) < c:
                abcs.append((a, b, c))

    for _ in range(len(odds)):
        i = odds[_]
        for j in odds[_ + 1:]:
            if j > 2 * i:
                break
            if fctrs[i] - fctrs[j] != fctrs[i]:
                continue
            a, b, c = j - i, i, j
            if mult_set(fctrs[a]) * mult_set(fctrs[b]) * mult_set(fctrs[c]) < c:
                abcs.append((a, b, c))

    return abcs

def solve(n):
    total = 0
    for tup in find_abcs(n):
        total += tup[2]
    return total

#print(sum([1 if _ else 0 for _ in squarefree(120000)[0]]))

start = time.time()

N = 120000
print(solve(N))

print("Time elapsed: {:0.4f} seconds".format(time.time() - start))