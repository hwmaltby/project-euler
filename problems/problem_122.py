#Henry Maltby 2017
import math
import time

def efficient_exponentiation(n):
    start = time.time()
    lst = [n] * (n + 1)
    to_find = set(range(1, n + 1))
    stack = [(1, 0)]
    rte = [0] * (n + 1)
    while stack:
        reached, depth = stack.pop()
        if reached > n or depth > lst[reached]:
            continue
        lst[reached] = depth
        rte[depth] = reached
        for i in range(depth + 1):
            stack.append((reached + rte[i], depth + 1))
    return sum(lst[1:])

N = 200
print(efficient_exponentiation(N))