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

N = 2
K = 1000
print(power_digit_sum(N, K))