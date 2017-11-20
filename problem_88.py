#Henry Maltby 2017
import math

def product_sum_numbers(n):
    unobtained = set(range(2, n + 1))
    good_nums = set()
    divisor_sums = {2: {(1, 2)}, 3: {(1, 3)}}
    i = 4
    while unobtained:
        divisor_sums[i] = set()
        for j in range(2, math.ceil(math.sqrt(i)) + 1):
            if i % j == 0:
                for tup in divisor_sums[i // j]:
                    new_tup = (tup[0] + 1, j + tup[1])
                    divisor_sums[i].add(new_tup)
                    k = new_tup[0] + (i - new_tup[1])
                    if k in unobtained:
                        unobtained.remove(k)
                        good_nums.add(i)
        divisor_sums[i].add((1, i))
        i += 1
    return sum(good_nums)

N = 120000
print(product_sum_numbers(N))