#Henry Maltby 2017
import math

def find_best_grid(k):
    """
    Returns the the value m * n, where m and n are values such that
    (1 + ... + m) * (1 + ... + n) is the closest possible to k, among
    all positive integer values of m and n.
    """
    m, n, best = 0, 0, 0
    triangles = [i * (i + 1) / 2 for i in range(2 * math.ceil(math.sqrt(k)))]
    i, j = 1, 1
    while j < len(triangles) and triangles[j] < k:
        while i < len(triangles) and triangles[i] * triangles[j] < 2 * k:
            if abs(k - triangles[i] * triangles[j]) < abs(k - best):
                m, n, best = i, j, triangles[i] * triangles[j]
            i += 1
        i = 1
        j += 1
    return m * n

print(find_best_grid(2000000))