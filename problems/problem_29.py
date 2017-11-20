#Henry Maltby 2017
import math

def count_powers(m, n):
    """
    Returns the number of distinct elements in the set of numbers of
    the form a^b, for non-unit positive integers a <= m and b <= n.
    """
    k = math.floor(math.sqrt(m)) + 1
    nums = [i for i in range(2, m + 1)]
    pwrs = set()
    for a in nums[:k-1]:
        b, k = 1, a
        while k in nums:
            for i in range(2, n + 1):
                pwrs.add((a, i * b))
            nums.remove(k)
            k *= a
            b += 1
    return len(pwrs) + (n - 1) * len(nums)

M = 100
N = 100
print(count_powers(M, N))