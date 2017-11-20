#Henry Maltby 2017
import math

def square_root(c):
    """
    Returns the positive square root if c is a perfect square and -1
    otherwise.
    """
    c_sqrt = int(round(math.sqrt(c)))
    if c_sqrt * c_sqrt == c:
        return c_sqrt
    return -1

def find_best_perimeter(n):
    """
    Returns the integer <= n that is the perimeter of the greatest
    number of non-congruent right triangles.
    """
    perims, best = {0: 0}, 0
    for a in range(3, (n // 3) + 1):
        for b in range(a + 1, (n // 2) + 1):
            c = square_root(a * a + b * b)
            if c != -1:
                p = a + b + c
                if p not in perims:
                    perims[p] = 0
                perims[p] += 1
                if p <= n and perims[p] > perims[best]:
                    best = p
    return best

N = 1000
print(find_best_perimeter(N))