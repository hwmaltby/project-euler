#Henry Maltby 2017
import time

def same_differences(n):
    lst = [0] * n
    total = 0
    a = 1
    while a < n:
        d = a // 4 + 1
        while (4 * d - a) * a < n and d < a:
            num = (4 * d - a) * a
            if lst[num] == 1:
                total -= 1
            lst[num] += 1
            if lst[num] == 1:
                total += 1
            d += 1
        a += 1
    return total

start = time.time()
N = 10 ** 6
print(same_differences(N))
print("{:0.4f} seconds have passed".format(time.time() - start))

start = time.time()
N = 10 ** 7
print(same_differences(N))
print("{:0.4f} seconds have passed".format(time.time() - start))

start = time.time()
N = 5 * (10 ** 7)
print(same_differences(N))
print("{} seconds have passed".format(time.time() - start))