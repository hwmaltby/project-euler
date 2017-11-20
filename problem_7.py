#Henry Maltby 2017
import math

def prime(n):
    lst = [2]
    i = lst[-1] + 1
    while len(lst) < n:
        if rel_prime(i, lst):
            lst.append(i)
        i += 1
    return lst[-1]

def rel_prime(n, prms):
    k = int(math.floor(math.sqrt(n) + 1))
    i = in_between(k, prms)
    j = 0
    while j <= i:
        if n % prms[j] == 0:
            return False
        j += 1
    return True

def in_between(i, lst):
    if i in lst:
        return lst.index(i)
    j = 0
    for j in range(len(lst)):
        if i < lst[j]:
            break
        j += 1
    return j

N = 10001
print(prime(N))