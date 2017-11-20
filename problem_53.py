#Henry Maltby 2017

def pascals_triangle(n, m):
    """
    Returns the number of elements of the n^th Pascal's triangle that
    have value greater than m.
    """
    triangle_list = [[1] * i for i in range(1, n + 2)]
    ans = 0
    for i in range(1, n + 1):
        for j in range(i+1):
            if j == 0:
                triangle_list[i][j] = triangle_list[i - 1][j]
            elif j == i:
                triangle_list[i][j] = triangle_list[i - 1][j - 1]
            else:
                triangle_list[i][j] = triangle_list[i - 1][j - 1] +\
                 triangle_list[i - 1][j]
            if triangle_list[i][j] > m:
                ans += 1
    return ans

N = 100
M = 1000000
print(pascals_triangle(N, M))