#Henry Maltby 2017
#warning: awful implementation.... and bad algorithm....
import math

def sum_of_modified_totients(n):
    """
    Returns phi'(2) + phi'(3) + phi'(4) + ... + phi'(n) where phi'
    returns the amount of numbers relatively prime to n between
    (n + 1)//3 and (n+2)//2.
    """
    tnts = [1] * (n + 1)
    for i in range(2, n):
        if tnts[i] == 1:
            tnts[i] = i - 1
            for j in range(2, (n // i) + 1):
                if (j == 2 or tnts[j] != 1) and tnts[j * i] == 1:
                    if j % i == 0:
                        tnts[j * i] = i * tnts[j]
                    else:
                        tnts[j * i] = (i - 1) * tnts[j]
    modified_tnts = [0] * (n + 1)
    for i in range(4, n + 1):
        if tnts[i] % 6 == 1:
            modified_tnts[i] = tnts[i]
        else:
            modified_tnts[i] = (tnts[i] - 2 * rel_prime_less_than_third(i)) // 2
    return sum(modified_tnts)

def gcd(a, b):
    """Returns the greatest common divisor of naturals a and b."""
    if b == 0:
        return a
    a, b = max(a, b), min(a, b)
    return gcd(b, (a % b))

def rel_prime_less_than_third(n):
    total = 0
    for i in range(1, n // 3 + 1):
        if gcd(i, n) == 1:
            total += 1
    return total

def rel_prime(n):
    total = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            total += 1
    return total

N = 12000
print(sum_of_modified_totients(N))