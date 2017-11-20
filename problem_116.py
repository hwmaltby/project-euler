#Henry Maltby 2017

def counting_block_combinations(n, m):
    """
    Returns the number of possible block combinations of length n with
    minimal red block length m.
    """
    num_ways = [0] * (n + 1)
    num_ways[0] = 1
    for i in range(1, n + 1):
        num_ways[i] += num_ways[i - 1]
        if m <= i:
            num_ways[i] += num_ways[i - m]
    return num_ways[n]

def red_green_or_blue(n):
    """
    Returns the number of possible block combinations of length n with
    tiles of length 1 and either tiles of length 2, 3, or 4 (but only
    one such tile type) and not all tiles are length 1.
    """
    ans = counting_block_combinations(n, 2) + counting_block_combinations(n, 3)\
        + counting_block_combinations(n, 4) - 3
    return ans

N = 50
print(red_green_or_blue(N))