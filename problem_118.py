#Henry Maltby 2017
import itertools
import time
import math

def sum_digits(n):
    """Returns the sum of the digits of n."""
    sum = 0
    for c in str(n):
        sum += int(c)
    return sum

def subset(n):
    for i in range(2 ** n):
        s = "{0:b}".format(i)
        yield ("0" * (n - len(s))) + s

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
    if n == 1:
        return False
    for p in prms:
        if n % p == 0:
            if n == p:
                return True
            return False
    return True

def find_primes(n):
    prms = sieve(math.ceil(math.sqrt(98765432)) + 1)
    digits = list(map(str, list(range(1, n + 1))))
    num_prms = {}
    for s in subset(n):
        if s == "0" * n:
            continue
        lst = []
        for i in range(n):
            if s[i] == '1':
                lst.append(digits[i])
        word = int("".join(lst))
        num_prms[word] = 0
        if sum_digits(word) % 3 != 0 or word == 3:
            for perm in itertools.permutations(lst):
                num = int("".join(perm))
                if is_prime(num, prms):
                    num_prms[word] += 1
    return num_prms

def prime_sets(n):
    start = time.time()
    num_prms = find_primes(n)
    total = 0
    accessed = {}
    for perm in itertools.permutations(list(range(1, n + 1))):
        prev = perm[0]
        words = [str(prev)]
        for i in range(1, n):
            if perm[i] > prev:
                words[-1] += str(perm[i])
            else:
                words.append(str(perm[i]))
            prev = perm[i]
        words.sort()
        to_save = "0".join(words)
        if to_save not in accessed:
            prod = 1
            for word in words:
                prod *= num_prms[int(word)]
            total += prod
            accessed[to_save] = prod
    return total
    #for part in integer_partitions(n):
    #    divide_up = {}
    #    used = set()
    #    for i in part[::-1]:
    #        count = 0
    #        while i in divide_up:
    #            i += 10
    #            count += 1
    #        divide_up = 
    #        for j in set(range(1, n + 1)) - used:
    #possible = []
    #next = 9
    #used = set()
    #while next != 0:
    #    for key in num_prms:
    #        if key % 10 == next and num_prms[key] != 0:
    #            for c in str(key):
    #                if c in used:
    #                    break
    #                used.append(c)
    #            used = set(c for c in str(key))
    #            next = 0
    #            for i in [9, 8, 7, 6, 5, 4, 3, 2, 1]:
    #                if i not in used:
    #                    next = i
    #                    break

def integer_partitions(n):
    #implementation taken from jeromekelleher.net/category/combinatorics.html
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]

start2 = time.time()
print(prime_sets(9))
print("Accomplished in {:0.4f} seconds".format(time.time() - start2))