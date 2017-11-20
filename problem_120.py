#Henry Maltby 2017

def r_max(a):
    if a % 2 == 0:
        return a * a - 2 * a
    return a * a - a

def square_remainders(n):
    total = 0
    for i in range(3, n + 1):
        total += r_max(i)
    return total

N = 1000
print(square_remainders(N))