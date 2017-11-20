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
    letters = list(range(0, k + 1))
    letters.remove(5)
    word = ''
    for i in decomp:
        c = letters[i]
        word += str(c)
        letters.remove(c)
    word += str(letters[0])
    return word

def div_prop(n):
    if int(n[1:4]) % 2 == 0 and int(n[2:5]) % 3 == 0 and int(n[3:6]) % 5 == 0\
     and int(n[4:7]) % 7 == 0 and int(n[5:8]) % 11 == 0 and int(n[6:9]) % 13\
    == 0 and int(n[7:]) % 17 == 0:
        return True
    return False

def substring_divisibility():
    """
    Returns the sum of all 0 to 9 pandigital numbers with the required
    divisibility property.
    """
    total = 0
    for i in range(1, 362881):
        perm = perm_lex_order(i, 9)
        perm = perm[:5] + '5' + perm[5:]
        if div_prop(perm):
            total += int(perm)
    return total

print(substring_divisibility())