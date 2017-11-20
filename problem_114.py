#Henry Maltby 2017

def counting_block_combinations(n):
    """
    Returns the number of possible block combinations of length n.
    """
    num_ways = [1] * (n + 1)
    num_ways[1] = num_ways[2] = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if j != 2 and j != 3:
                num_ways[i] += num_ways[i - j]
    return num_ways[n]

N = 50
print(counting_block_combinations(N))