#Henry Maltby 2017

def digit_power_sum(n, k):
    total = 0
    for digit in str(n):
        total += int(digit) ** k
    return total

def find_digit_power_sums(n):
    """
    Returns all numbers equal to the sum of their digits, raised to
    the nth power. Should be used only for n <= 6.
    """
    upper_bound = len(str(9 ** n)) * (9 ** n)
    total = 0
    for i in range(10, upper_bound):
        if digit_power_sum(i, n) == i:
            total += i
    return total

N = 5
print(find_digit_power_sums(N))