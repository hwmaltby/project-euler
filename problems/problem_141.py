#Henry Maltby 2017
import math

#In some order, (d, q, r) = (a, ax, ax^2). So, there are two cases:
#(1) n = a^2x^2 + ax = ax(ax + 1) and (2) n = a^2x^3 + a = a(ax^3 + 1).

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

def solve(n):
    k = math.floor(math.sqrt(n) + 1) + 1
    a = [1] * k
    prms = sieve(math.floor(math.sqrt(k) + 1))
    for p in prms:
        curr = p*p
        while curr < k:
            for m in range(curr, k, curr):
                a[m] *= p
            curr *= p*p
    valid = set()
    for i in range(1, k):
        denom = a[i]
        for j in range(denom + 1, (denom * k // i) + 1):
            ans = (i*i*j*j*j)//(denom*denom*denom)+i
            #print("{}, {}, {}".format(i, x, ans))
            if ans > n:
                break
            if is_square(ans):
                valid.add(ans)
    return sum(valid)

N = 10**12
print(solve(N))