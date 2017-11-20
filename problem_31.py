#Henry Maltby 2017

def coin_sums(n, values):
    """
    Returns the number of ways n can be written as the sum of
    non-negative multiples of elements of values.
    """
    a = values[-1]
    if len(values) == 1:
        return 1 if n % a == 0 else 0
    total = 0
    k = 0
    values = values[:-1]
    while k <= n:
        total += coin_sums(n - k, values)
        k += a
    return total

N = 200
VALUES = [1, 2, 5, 10, 20, 50, 100, 200]
print(coin_sums(N, VALUES))