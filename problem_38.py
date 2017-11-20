#Henry Maltby 2017

def all_digits(s):
    """
    Returns true if the string s is a permutation of the 9 digits and
    false otherwise.
    """
    if len(s) != 9:
        return False
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for d in digits:
        if d not in s:
            return False
    return True

def create_pandigital(n):
    """
    Returns the pandigital created by n, or -1 if n does not generate
    a pandigital.
    """
    s, i = '', 1
    while len(s) < 9:
        s += str(i * n)
        i += 1
    if all_digits(s):
        return int(s)
    return -1

def find_largest_pandigital():
    """Returns the largest pandigital number generated as dictated."""
    greatest = 0
    for i in range(1, 10000):
        greatest = max(greatest, create_pandigital(i))
    return greatest

print(find_largest_pandigital())