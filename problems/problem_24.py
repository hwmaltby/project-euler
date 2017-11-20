#Henry Maltby 2017

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
    letters = list(range(k))
    word = ''
    for i in decomp:
        c = letters[i]
        word += str(c)
        letters.remove(c)
    word += str(letters[0])
    return word

print(perm_lex_order(1000000, 10))