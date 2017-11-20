#Henry Maltby 2017

def counting_block_combinations(n, m):
    """
    Returns the number of possible block combinations of length n with
    minimal red block length m.
    """
    num_ways = [1] * (n + 1)
    for i in range(1, min(m, n + 1)):
        num_ways[i] = 0
    for i in range(1, n + 1):
        num_ways[i] += num_ways[i - 1]
        for j in range(m + 1, i + 1):
            num_ways[i] += num_ways[i - j]
    return num_ways

def find_first_exceeding(m, bnd):
    """
    Returns the lowest value n such that there are more than bnd block
    combinations of length n with minimal red block length m.
    """
    lst = [0]
    n = m + 1
    while lst[-1] < bnd:
        n *= 2
        lst = counting_block_combinations(n, m)
    for i in range(len(lst)):
        if lst[i] > bnd:
            return i

M = 50
K = 1000000
print(find_first_exceeding(M, K))