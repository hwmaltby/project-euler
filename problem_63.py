#Henry Maltby 2017

def find_n_digit_nth_powers():
    """Returns the number of n digit perfect nth powers."""
    total = 0
    for a in range(1, 10):
        b = 1
        while a ** b >= 10 ** (b - 1):
            total += 1
            b += 1
    return total

print(find_n_digit_nth_powers())