#Henry Maltby 2017

def smart_exp(n, k):
    ans, tmp = 1, n
    while k > 0:
        k, r = divmod(k, 2)
        if r == 1:
            ans *= tmp
        tmp *= tmp
    return ans

def sum_digits(n):
    sum = 0
    for c in str(n):
        sum += int(c)
    return sum

def power_digit_sum(n, k):
    return sum_digits(smart_exp(n, k))

def powerful_digit_sum(m, n):
    """
    Returns the maximal digit sum of perfect powers a^b, where a <= m,
    b <= n.
    """
    maxl = 0
    for a in range(2, m + 1):
        for b in range(2, n + 1):
            maxl = max(maxl, power_digit_sum(a, b))
    return maxl

M = 100
N = 100
print(powerful_digit_sum(M, N))