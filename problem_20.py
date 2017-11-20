#Henry Maltby 2017

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def sum_digits(n):
    sum = 0
    for c in str(n):
        sum += int(c)
    return sum

def factorial_digit_sum(n):
    return sum_digits(factorial(n))

N = 100
print(factorial_digit_sum(N))