#Henry Maltby 2017

def pascals_triangle(n):
    """Returns Pascal's triangle, through row n."""
    triangle_list = [[1] * i for i in range(1, n + 2)]
    for i in range(1, n + 1):
        for j in range(i+1):
            if j == 0:
                triangle_list[i][j] = triangle_list[i - 1][j]
            elif j == i:
                triangle_list[i][j] = triangle_list[i - 1][j - 1]
            else:
                triangle_list[i][j] = triangle_list[i - 1][j - 1] +\
                 triangle_list[i - 1][j]
    return triangle_list

def subset_pairs(n):
    triangle_list = pascals_triangle(n)
    total = 0
    for k in range(2, n + 1, 2):
        j = k // 2
        total += (triangle_list[k][j] * (j - 1)) // (2 * (j + 1)) *\
            triangle_list[n][k]
    return total

N = 12
print(subset_pairs(N))