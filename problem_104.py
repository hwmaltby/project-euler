#Henry Maltby 2017
import math

def fib(n, first_k=[]):
    k = len(first_k)
    curr, prev = 0, 1
    if k > 2:
        curr, prev = first_k[-1],first_k[-2]
    lst = first_k
    next = curr + prev
    for i in range(n - k):
        lst.append(next)
        next, curr, prev = next + curr, next, curr
    return lst

def fib_last_digits(n, first_k=[]):
    k = len(first_k)
    curr, prev = 0, 1
    if k > 2:
        curr, prev = first_k[-1],first_k[-2]
    lst = first_k
    next = (curr + prev) % (10 ** 9)
    for i in range(n - k):
        lst.append(next)
        next, curr, prev = (next + curr) % (10 ** 9), next, curr
    return lst

def modified_smart_exp(n, k):
    ans, tmp = 1, n
    while k > 0:
        k, r = divmod(k, 2)
        if r == 1:
            ans *= tmp
        tmp *= tmp
        while tmp > 10:
            tmp /= 10
        while ans > 10:
            ans /= 10
    return ans

def fib_first_digits(n):
    phi = (1 + math.sqrt(5)) / 2
    ans = modified_smart_exp(phi, n) * (10 ** 10) / math.sqrt(5)
    return str(ans)[:9]

def is_pandigital(s):
    if len(s) != 9:
        return False
    digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    try:
        for c in s:
            digits.remove(c)
    except KeyError:
        return False
    return True

def find_doubly_pandigital_fib(n):
    #fibs = fib(n)
    fibs_mod = fib_last_digits(n)
    for i in range(n):
        if is_pandigital(str(fibs_mod[i])):
            if is_pandigital(fib_first_digits(i + 1)):
                return i + 1

N = 10000000
print(find_doubly_pandigital_fib(N))