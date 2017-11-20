#Henry Maltby 2017

def is_palindromic(n):
    """Returns true if n is a palindrome."""
    return str(n) == str(n)[::-1]

def is_lychrel(n):
    """Returns true if n is a Lychrel number. Require n <= 10000."""
    for i in range(50):
        n = int(n + int(str(n)[::-1]))
        if is_palindromic(n):
            return False
    return True

def count_lychrel_numbers(n):
    """Returns the amount of numbers less than n that are Lychrel."""
    total = 0
    for i in range(1, n):
        if is_lychrel(i):
            total += 1
    return total

N = 10000
print(count_lychrel_numbers(N))