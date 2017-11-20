#Henry Maltby 2017

def partition(n):
    parts = [[1] * (n + 1) for i in range(n + 1)]
    for i in range(2, n + 1):
        tmp = [(1 if k % i == 0 else 0) for k in range(n + 1)]
        for j in range(n + 1):
            parts[i][j] = 0
            for k in range(j + 1):
                parts[i][j] += tmp[k] * parts[i - 1][j - k]
    return parts[n][n]

N = 100
print(partition(N) - 1)