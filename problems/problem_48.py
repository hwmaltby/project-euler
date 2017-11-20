#Henry Maltby 2017

def smart_exp(n, k, mod):
    """Returns n^k mod mod."""
    ans, tmp = 1, (n % mod)
    while k > 0:
        k, r = divmod(k, 2)
        if r == 1:
            ans = (ans * tmp) % mod
        tmp = (tmp * tmp) % mod
    return ans

def sum_of_perfect_powers(n, m):
    """Returns the last m digits of the sum 1^1 + 2^2 + ... + n^n."""
    total = 0
    for k in range(1, n + 1):
        total = (total + smart_exp(k, k, 10 ** m)) % (10 ** m)
    return total

N = 1000
M = 10
print(sum_of_perfect_powers(N, M))