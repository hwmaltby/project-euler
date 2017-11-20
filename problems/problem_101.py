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

def fn(x):
    x = x + 1
    return 1 - x + x ** 2 - x ** 3 + x ** 4 - x ** 5 + x ** 6 - x ** 7 + x ** 8\
        - x ** 9 + x ** 10

def bop(seq, n, triangle_list):
    total = 0
    for i in range(len(seq)):
        total += seq[i] * triangle_list[n - 1][i]
    return total

def sum_of_fits(d):
    triangle_list = pascals_triangle(d)
    diff_table = []
    total = 0
    for i in range(d):
        diff = fn(i)
        for row in diff_table:
            row.append(diff)
            if len(row) != 1:
                diff -= row[-2]
        diff_table.append([diff])
        seq = []
        for row in diff_table:
            seq.append(row[0])
        n = i + 1
        while bop(seq, n, triangle_list) == fn(n - 1):
            n += 1
        total += bop(seq, n, triangle_list)
    return total

print(sum_of_fits(10))