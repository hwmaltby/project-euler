#Henry Maltby 2017

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
    for p in prms:
        if n % p == 0:
            return False
    return True

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def factorial_decomposition(n, k):
    q, r = divmod(n, factorial(k))
    if k == 0:
        return []
    return [q] + factorial_decomposition(r, k - 1)

def perm_lex_order(n, k):
    decomp = factorial_decomposition(n - 1, k - 1)
    letters = list(range(1, k + 1))
    word = ''
    for i in decomp:
        c = letters[i]
        word += str(c)
        letters.remove(c)
    word += str(letters[0])
    return word

def largest_pandigital_prime():
    prms = sieve(2766)
    for i in range(5040):
        perm = int(perm_lex_order(5040 - i, 7))
        if is_prime(perm, prms):
            return perm
    return "we sad"

print(largest_pandigital_prime())