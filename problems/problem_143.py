#Henry Maltby 2017
import time
import math

def add_to_set_dict(key, entry, dct):
    if key in dct:
        dct[key].add(entry)
    else:
        dct[key] = {entry}

def update(m, n, k):
    return k * (2 * m * n + n * n), k * (m * m - n * n)

def generate(lmt):
    dct = {}
    m = n = k = 1
    stop = math.ceil(math.sqrt(2 * lmt))
    while m < stop:
        while n < m:
            a, b = update(m, n, k)
            while a < lmt and b < lmt:
                a, b = update(m, n, k)
                add_to_set_dict(a, b, dct)
                add_to_set_dict(b, a, dct)
                k += 1
            n += 1
            k = 1
        m += 1
        if m * m > lmt:
            n = math.ceil(math.sqrt(m * m - lmt))
        else:
            n = 1
    return dct

def solve(n):
    """."""
    dct = generate(n)
    all_sums = set()

    for i in dct:
        for j in dct[i]:
            for k in dct[j].intersection(dct[i]):
                if i + j + k < n:
                    all_sums.add(i + j + k)

    return sum(all_sums)

start = time.time()
N = 120000
print(solve(N))
print("Elapsed time: {:0.4f}".format(time.time() - start))


'''OLD FUNCTIONS: (saved for re-use elsewhere)
def sieve(n):
    a = [True] * (n + 1)
    a[0] = a[1] = False
    lst = []

    for (i, isprime) in enumerate(a):
        if isprime:
            lst.append(i)
            for n in range(i*i, n + 1, i):
                a[n] = False

    return lst

def factor(n, prms):
    fctrs = {}
    stop = math.ceil(math.sqrt(n)) + 1
    i = 0
    while i < len(prms) and prms[i] < stop:
        exp = 0
        while n % prms[i] == 0:
            n = n // prms[i]
            exp += 1
        if exp != 0:
            fctrs[prms[i]] = exp
        i += 1
    if n != 1:
        fctrs[n] = 1
    return fctrs

def is_square(n):
    """Returns true if n is a perfect square."""
    if n == 0 or n == 1:
        return True
    x = n // 2
    prev = n
    while x * x != n:
        prev2 = prev
        prev = x
        x = (x + (n // x)) // 2
        if x == prev or x == prev2:
            return False
    return True

def totient(fctrs):
    ans = 1
    for key in fctrs:
        ans *= fctrs[key] + 1
    return ans

def count_diffs_of_squares(fctrs):
    if 2 not in fctrs:
        return (totient(fctrs) + 1) // 2
    if fctrs[2] == 1:
        return 0
    tmp = fctrs.copy()
    tmp[2] -= 2
    return (totient(tmp) + 1) // 2'''