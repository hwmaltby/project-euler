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

print(str((28433 * smart_exp(2, 7830457, 10000000000) + 1) % 10000000000))