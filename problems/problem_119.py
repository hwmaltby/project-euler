#Henry Maltby 2017
#should rewrite to table of (sum, power) and work the other way around
import time

def sum_digits(n):
    """Returns the sum of the digits of n."""
    sum = 0
    for c in str(n):
        sum += int(c)
    return sum

def first_tup(tup):
    return tup[0]

def digit_power_sum(n):
    queue = []
    for i in [2, 3, 5, 7, 11, 13, 19, 23, 29, 31, 37, 41, 43, 47]:
        num = 2 ** i
        queue.append((num, 2, i))
    found = []
    while len(found) < n:
        k, a, b = queue.pop(0)
        j = sum_digits(k)
        prod = 1
        if j > 1:
            while prod * j <= k:
                prod *= j
            if prod == k and k >= 10 and (len(found) == 0 or prod != found[-1]):
                found.append(k)
        queue.append(((a + 1) ** b, a + 1, b))
        queue.sort(key=first_tup)
    return found[-1]

start = time.time()
N = 30
print(digit_power_sum(N))
print("Accomplished in {:0.4f} seconds".format(time.time() - start))