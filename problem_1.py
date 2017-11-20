#Henry Maltby 2017
import math

def threes_and_fives(n):
    return 3 * sum(n / 3) + 5 * sum(n / 5) - 15 * sum(n / 15)

def sum(n):
    k = math.floor(n)
    return int(k * (k + 1) / 2)

N = 1000 - 1
print(threes_and_fives(N))