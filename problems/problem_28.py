#Henry Maltby 2017

def spiral_diagonal(n):
    """
    Returns the sum of the numbers along the two diagonals of an n x n
    square filled with numbers in the following way: 1 in the center
    (n assumed odd); 2 to the right of 1; and numbering continued in
    a clockwise fashion centered around 1.
    """
    k = int(round((n - 1) / 2))
    total = 0
    for i in range(1, k + 1):
        sd = 2 * i
        sq = (sd + 1) * (sd + 1)
        total += sq
        total += sq - sd
        total += sq - 2*sd
        total += sq - 3*sd
    return total + 1

N = 1001
print(spiral_diagonal(N))