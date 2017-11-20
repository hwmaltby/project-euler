#Henry Maltby 2017

def is_binary_palindrome(n):
    """Returns true if n in base 2 is a palindrome."""
    s = "{0:b}".format(n)
    return s == s[::-1]

def palindromes_less_than(n):
    """Returns a sorted list of all palindromes less than n."""
    pals = []
    if n < 10:
        return list(range(1, n + 1))
    l = len(str(n))
    for i in range(1, l + 1):
        q, r = divmod(i + 1, 2)
        for j in range(10 ** (q -1), 10 ** q):
            j = str(j)
            if r == 0:
                pal = int(j + j[-2::-1])
            else:
                pal = int(j + j[::-1])
            if pal < n:
                pals.append(pal)
    return pals



def sum_double_base_palindromes(n):
    """
    Returns the sum of all positive integers k that are (a) <= n, (b)
    palindromes in base 10, and (c) palindromes in base 2.
    """
    total = 0
    for pal in palindromes_less_than(n):
        if is_binary_palindrome(pal):
            total += pal
    return total

N = 1000000
print(sum_double_base_palindromes(N))