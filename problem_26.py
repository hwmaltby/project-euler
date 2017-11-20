#Henry Maltby 2017

def gcd(a, b):
    """Returns the greatest common divisor of naturals a and b."""
    if b == 0:
        return a
    a, b = max(a, b), min(a, b)
    return gcd(b, (a % b))

def ord(n, a):
    """
    Returns ord_n(a), the smallest positive integer k such that
    a^k = 1 mod n.
    """
    if gcd(n, a) != 1 or n == 1:
        return 0
    k = 1
    a %= n
    prod = a
    while prod != 1:
        prod = (prod * a) % n
        k += 1
    return k

def longest_decimal_cycle(n):
    """
    Returns the positive integer k such that 1/k has the longest
    recurring cycle in its decimal representation, among all fractions
    1/d for positive integers d less than n.
    """
    largest, k = 0, 0
    for i in range(1, n):
        tmp = ord(i, 10)
        if tmp > largest:
            largest, k = tmp, i
    #Note that calling ord(i, 10) does not always return the length of
    #the recurring cycle in 1/i: it only does when gcd(i, 10) != 1.
    #This is sufficient for determining the desired value k though; if
    #there is an i < n with gcd(i, 10) != 1 such that ord(i, 10) > 
    #ord(k, 10), then also ord(i/gcd(10, i), 10) > ord(k, 10), which
    #contradicts the maximality of k among integers rel prime to 10.
    return k

D = 1000
print(longest_decimal_cycle(1000))