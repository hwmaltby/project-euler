#Henry Maltby 2017
import math

def gcd_table(m, n):
    gcds = [[0] * n for i in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if i == j:
                gcds[i][j] = i
            elif j == 1 or i == 1:
                gcds[i][j] = 1
            elif j > i:
                gcds[i][j] = gcds[i][j - i]
            else:
                gcds[i][j] = gcds[i - j][j]
    return gcds

def lonely_pythag_perims(n):
    """
    Returns the amount of integer perimeters <= n that give rise to
    precisely one Pythagorean triplet.
    """
    bound = math.floor(math.sqrt(n / 2) + 1)
    gcds = gcd_table(bound + 1, bound)
    perims = {}
    total = 0
    for i in range(2, bound):
        for j in range(1, i):
            a = i * i - j * j
            b = 2 * i * j
            a, b = min(a, b), max(a, b)
            c = i * i + j * j
            peri = a + b + c
            for k in range(1, n // peri + 1):
                a1, b1, c1, perim = k * a, k * b, k * c, k * peri
                if perim > n:
                    continue
                if perim not in perims:
                    perims[perim] = [[a1, b1, c1]]
                    total += 1
                    continue
                if len(perims[perim]) == 1 and [a1, b1, c1] != perims[perim][0]:
                    perims[perim].append([a1, b1, c1])
                    total -= 1
    return total

N = 1500000
print(lonely_pythag_perims(N))