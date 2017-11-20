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

def combination(n, k):
    for comb in comb_lst(list(range(1, n + 1)), k):
        yield comb

def comb_lst(lst, k):
    for i in range(len(lst) - k + 1):
        if k == 0:
            break
        if k == 1:
            yield [lst[i]]
            continue
        for comb in comb_lst(lst[i + 1:], k - 1):
            yield [lst[i]] + comb

def factorial(n):
    lst = [1]
    for i in range(1, n + 1):
        lst.append(lst[-1] * i)
    return lst

def disc_game(n):
    triangle_list = pascals_triangle(n)
    facts = factorial(n + 1)
    total = 0
    for k in range((n + 1) // 2):
        for comb in combination(n, k):
            prod = 1
            for i in comb:
                prod *= i
            total += prod
    return facts[-1] // (total + 1)

print(disc_game(15))