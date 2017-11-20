#Henry Maltby 2017
import math

def fibo_digits(n):
    k = (math.log(math.sqrt(5))/math.log(10) + n - 1) * math.log(10)\
     / math.log((1 + math.sqrt(5)) / 2)
    return int(math.ceil(k))

N = 1000
print(fibo_digits(N))