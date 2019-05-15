#Henry Maltby
import time
import math

def solve(n):
    """
    .
    """
    ans, mtrx = 0, populate(n)
    for i in range(n):
        ans = max(ans, dp(mtrx[i]))
    for i in range(n):
        lst = [mtrx[j][i] for j in range(n)]
        ans = max(ans, dp(lst))
    for i in range(2 * n - 1):
        lst = [mtrx[j][i - j] for j in range(max(0, i - n + 1), min(i + 1, n))]
        ans = max(ans, dp(lst))
    for i in range(2 * n - 1):
        lst = [mtrx[n - 1 - j][i - j] for j in range(max(0, i - n + 1), min(i + 1, n))]
        ans = max(ans, dp(lst))
    return ans

def populate(n):
    """
    Takes as input an integer n. Returns a double array of size n x n
    containing the first n^2 elements of the Lagged Fibonacci Generator.
    """
    lst, ans = [], [[]]
    for i in range(1, n * n + 1):
        if i <= 55:
            ele = (100003 - 200003 * i + 300007 * i * i * i) % 1000000
        else:
            ele = (lst[i - 1 - 24] + lst[i - 1 - 55] + 1000000) % 1000000
        lst.append(ele - 500000)
    for i in range(n * n):
        q = i // n
        if len(ans) == q:
            ans.append([])
        ans[q].append(lst[i])
    return ans

def dp(lst):
    """
    Takes as input array lst. Returns an integer, the maximal subsequence sum.
    """
    ans, temp = 0, 0
    for k in lst:
        temp = max(0, temp + k)
        ans = max(temp, ans)
    return ans

start = time.time()
N = 2000
print(solve(N))
print("Elapsed time: {:0.4f}".format(time.time() - start))