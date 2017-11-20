#Henry Maltby 2017

def sieve(n):
    is_prime = [True] * n
    is_prime[0], is_prime[1] = False, False
    prms = []
    for i in range(2, n):
        if is_prime[i]:
            prms.append(i)
            for j in range(i*i, n, i):
                is_prime[j] = False
    return prms

def partition(n, m):
    prms = sieve(n)
    parts = [[0] * (n + 1) for i in range(len(prms) + 1)]
    parts[0][0] = 1
    minl = n + 1
    for i in range(len(prms)):
        tmp = [(1 if k % prms[i] == 0 else 0) for k in range(n + 1)]
        for j in range(n + 1):
            parts[i + 1][j] = 0
            for k in range(j + 1):
                parts[i + 1][j] += tmp[k] * parts[i][j - k]
            if parts[i + 1][j] > m and j < minl:
                minl = j
    return minl

N, M = 100, 5000
print(partition(N, M))