#Henry Maltby 2017
import time

def count_cuboids(a, b, m):
    """
    Returns the number of cuboids that have all sides <= m, one equal
    to max(a, b), and the other two summing to min(a, b).
    """
    a, b = min(a, b), max(a, b)
    if a > m or b > 2 * m:
        return 0
    if b > m:
        if (b + 1) // 2 > a:
            return 0
        return (a - ((b - 1) // 2))
    total = 0
    if (b + 1) // 2 <= a:
        total += (a - ((b - 1) // 2))
    total += (a // 2)
    return total

def create_cuboids(k):
    """
    Returns the number of cuboids that have all sides <= k, integer
    side lengths, and an integer long diagonal length.
    """
    pythag_triplets = set()
    for m in range(2, k + 1):
        for n in range(1, min(k // m + 2, m)):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            mult = 1
            while mult * m * n <= k:
                triple = (mult * a, mult * b, mult * c)
                triple2 = (mult * b, mult * a, mult * c)
                if triple2 not in pythag_triplets:
                    pythag_triplets.add(triple)
                mult += 1
    total = 0
    for triple in pythag_triplets:
        total += count_cuboids(triple[0], triple[1], k)
    return total

def find_first_greater(fn, value):
    """
    Returns the first positive integer k such that fn(k) > value.
    """
    test, step, less_than, go_up = 1, 1, True, True
    while not fn(test - 1) <= value or not fn(test) > value:
        if fn(test) < value:
            test += step
        else:
            less_than = False
            test -= step
        if not less_than:
            go_up = False
        if go_up:
            step *= 2
        else:
            step = step // 2
    return test

N = 1000000
print(find_first_greater(create_cuboids, N))