#Henry Maltby 2017
import decimal

def sum_digits(n):
    """Returns the sum of the digits of n."""
    sum = 0
    for c in str(n):
        sum += int(c)
    return sum

def sum_sqrt_decimals(n, m):
    i, sqrs = 1, []
    while i * i <= n:
        sqrs.append(i * i)
        i += 1
    sqrs = set(sqrs)

    decimal.getcontext().prec = m
    decimal.getcontext().rounding = decimal.ROUND_DOWN

    total = 0
    for i in range(1, n + 1):
        if i not in sqrs:
            dec = decimal.Decimal(str(i)) ** decimal.Decimal('0.5')
            total += sum_digits(int(str(dec)[-m+1:]))
            total += int(str(dec)[0])
    return total

N, M = 100, 100
print(sum_sqrt_decimals(N, M))