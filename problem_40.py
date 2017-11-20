#Henry Maltby 2017

def find_digit(n):
    """Returns the n^th digit of Champernowne's constant."""
    last, tot, i = 0, 0, 1
    while tot < n:
        last = tot
        tot += i * (10 ** i - 10 ** (i - 1))
        i += 1
    q, r = divmod(n - last - 1, i - 1)
    k = 10 ** (i - 2) + q
    return str(k)[r]

def weird_multiply_digits(n):
    """Returns the desired value (at least, when n=6)."""
    prod = 1
    for i in range(n + 1):
        prod *= int(find_digit(10 ** i))
    return prod

N = 6
print(weird_multiply_digits(N))