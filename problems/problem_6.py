#Henry Maltby 2017

def sum_of_squares(n):
    return (n * (n + 1) * (2*n + 1) / 6)

def square_of_sums(n):
    return (n * (n + 1) / 2) * (n * (n + 1) / 2)

def sum_square_difference(n):
    return square_of_sums(n) - sum_of_squares(n)

N = 100
print(sum_square_difference(N))