#Henry Maltby 2017
import math

def sum_even_fib(n):
    k = int(math.ceil(1 + math.sqrt(5) * math.log(n, (1 + math.sqrt(5)) / 2)))
    lst = fibonacci(k)
    sum = 0
    for i in range(k + 1):
        if i % 3 == 2 and lst[i] < n:
            sum += lst[i]
    return sum


def fibonacci(n):
    lst = [1, 1]
    k = 1
    while k < n:
        lst.append(lst[-1] + lst[-2])
        k += 1
    return lst

N = 4000000
print(sum_even_fib(N))