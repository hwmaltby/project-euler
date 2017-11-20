#Henry Maltby 2017
import math
import time

def efficient_exponentiation(n):
    start = time.time()
    lst = [0] * (n + 1)
    to_find = set(range(1, n + 1))
    queue = [(1, [1])]
    while queue and to_find:
        tup = queue.pop(0)
        if lst[tup[0]] == 0:
            print("We still need to find " + str(to_find))
            lst[tup[0]] = len(tup[1]) - 1
            to_find.remove(tup[0])
            print("We found {} with {:0.4f} seconds remaining".format(tup[0], time.time() - start))
        for i in tup[1]:
            num = tup[0] + i
            path = tup[1] + [num]
            if num <= n:
                queue.append((num, path))
    return sum(lst)

N = 200
print(efficient_exponentiation(N))

#Henry Maltby 2017
#import math
#
#def efficient_exponentiation(n):
#    lst = [(math.inf, -1)] * (n + 1)
#    lst[0] = (-1, {1})
#    total = 1
#    queue = [1, {1}]
#    while queue:
#        tup = queue.pop(0)
#        for i in tup[1]:
#            num = tup[0] + i
#            queue.append((num, tup[1].join({num})))
#    for i in range(2, n + 1):
#        vertices = {1}
#        edges = {1: [1]}
#        path_lengths = {1: 0}
#        v = 1
#        while v < i:
#            v *= 2
#            vertices.add(v)
#            edges[v] = edges[v // 2] + [v]
#            path_lengths[v] = path_lengths[v // 2] + 1
#        asdf
#    for i in range(n + 1):
#        tup = lst[i]
#        total += tup[0]
#        for j in tup[1]:
#            if i + j > n:
#                continue
#            if lst[i + j][0] < tup[0] + 1:
#                continue
#            elif lst[i + j][0] == tup[0] + 1:
#                tup2 = lst[i + j]
#                lst[i + j] = (tup[0] + 1, tup2[1].union(tup[1]))
#            else:
#                lst[i + j] = (tup[0] + 1, tup[1].union({i + j}))
#    print(lst[15])
#    return total
#
#N = 200
#print(efficient_exponentiation(N))