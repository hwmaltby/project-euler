#Henry Maltby 2017
import math

def pentagonal(n):
    """Returns the n^th pentagonal number."""
    return (n * (3*n - 1)) // 2

def min_diff(n):
    """
    Returns the minimal difference between two pentagonal numbers, the
    sum and difference of which are each pentagonal.
    """
    pents = [pentagonal(i) for i in range(1, n + 1)]
    pents_set = set(pents)
    minl = math.inf
    for i in range(n):
        for j in range(i):
            D = pents[i] - pents[j]
            if pents[i] + pents[j] in pents_set and D in pents_set:
                minl = min(minl, D)
    return minl

N = 4000
print(min_diff(N))