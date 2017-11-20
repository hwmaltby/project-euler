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

def not_bouncy(n):
    """
    Returns the number of not bouncy numbers with at most n digits.
    """
    triangle_list = pascals_triangle(n + 10)
    ans = triangle_list[n + 9][9] + triangle_list[n + 10][10] - 10 * n - 2
    return ans

N = 100
print(not_bouncy(100))