#Henry Maltby 2017

def max_path_sum(triangle_list):
    """
    """
    n = len(triangle_list)
    ans = 0
    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                triangle_list[i][j] += triangle_list[i - 1][j]
            elif j == i:
                triangle_list[i][j] += triangle_list[i - 1][j - 1]
            else:
                triangle_list[i][j] += max(triangle_list[i - 1][j - 1],\
                 triangle_list[i - 1][j])
            if i == n - 1 and triangle_list[i][j] > ans:
                ans = triangle_list[i][j]
    return ans

f = open("problem_67_triangle.txt")
triangle_list = [list(map(int, line.split(' '))) for line in f.read().strip().split('\n')]
print(max_path_sum(triangle_list))