#Henry Maltby 2017
import math
import time

def subset(n):
    for i in range(2 ** n):
        s = "{0:b}".format(i)
        yield ("0" * (n - len(s))) + s

def combination(n, k):
    for comb in comb_lst(list(range(1, n + 1)), k):
        yield comb

def comb_lst(lst, k):
    for i in range(len(lst) - k + 1):
        if k == 0:
            break
        if k == 1:
            yield [lst[i]]
            continue
        for comb in comb_lst(lst[i + 1:], k - 1):
            yield [lst[i]] + comb

def dyck_paths(n):
    """Yields all Dyck paths of length 2n that start with a 0."""
    if n == 0:
        yield ""
    for i in range(n):
        for path1 in dyck_paths(i):
            s = "0" + path1 + "1"
            for path2 in dyck_paths(n - 1 - i):
                yield s + path2

def non_dyck_paths(n):
    """Returns a path that is not a Dyck path and ends with a 1."""
    avoid = set(dyck_paths(n))
    for comb in combination(2 * n - 1, n - 1):
        index = 0
        s = ""
        for i in range(1, 2 * n):
            if index < len(comb) and comb[index] == i:
                s += "1"
                index += 1
            else:
                s += "0"
        s += "1"
        if s not in avoid:
            yield s

def is_special(A):
    n = len(A)
    for k in range(2, n + 1, 2):
        for path in non_dyck_paths(k // 2):
            for comb in combination(n, k):
                total1, total2 = 0, 0
                for i in range(k):
                    if path[i] == '1':
                        total1 += A[comb[i] - 1]
                    else:
                        total2 += A[comb[i] - 1]
                if total1 == total2:
                    return False
    for k in range(2, n + 2, 2):
        for path in non_dyck_paths(k // 2):
            path = path[-2::-1]
            for comb in combination(n, k - 1):
                total1, total2 = 0, 0
                for i in range(k - 1):
                    if path[i] == '1':
                        total1 += A[comb[i] - 1]
                    else:
                        total2 += A[comb[i] - 1]
                if total1 >= total2:
                    return False
    return True

def find_optimal_special():
    #start = time.time()
    elapsed, index = 0, 0
    minl = math.inf
    for comb in comb_lst(list(range(20, 46)), 7):
        if is_special(comb):
            minl = min(minl, sum(comb))
        index += 1
        #if time.time() - start > elapsed:
            #print("{0:.3f} seconds have passed and we are trying case #{1}".format(time.time() - start, index))
            #if minl < math.infinity:
            #    print("The best sum found so far is {0}".format(minl))
            #elapsed += 1
    return minl

print(find_optimal_special())