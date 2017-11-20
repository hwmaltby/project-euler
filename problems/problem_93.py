#Henry Maltby 2017
import operator

def generate_expressions(x, y, z, w):
    outcomes = set()
    ops = (operator.add, operator.sub, operator.mul, operator.truediv)
    for a in {x, y, z, w}:
        for b in {x, y, z, w} - {a}:
            for c in {x, y, z, w} - {a, b}:
                for d in {x, y, z, w} - {a, b, c}:
                    for fn1 in ops:
                        for fn2 in ops:
                            for fn3 in ops:
                                try:
                                    tmp = fn1(fn2(a, b), fn3(c, d))
                                    if float(tmp).is_integer() and tmp > 0:
                                        outcomes.add(int(tmp))
                                except ZeroDivisionError:
                                    pass
                                try:
                                    tmp = fn1(fn2(fn3(a, b), c), d)
                                    if float(tmp).is_integer() and tmp > 0:
                                        outcomes.add(int(tmp))
                                except ZeroDivisionError:
                                    pass
                                try:
                                    tmp = fn1(fn2(a, fn3(b, c)), d)
                                    if float(tmp).is_integer() and tmp > 0:
                                        outcomes.add(int(tmp))
                                except ZeroDivisionError:
                                    pass
                                try:
                                    tmp = fn1(a, fn2(fn3(b, c), d))
                                    if float(tmp).is_integer() and tmp > 0:
                                        outcomes.add(int(tmp))
                                except ZeroDivisionError:
                                    pass
                                try:
                                    tmp = fn1(a, fn2(b, fn3(c, d)))
                                    if float(tmp).is_integer() and tmp > 0:
                                        outcomes.add(int(tmp))
                                except ZeroDivisionError:
                                    pass
    results = sorted(list(outcomes))
    curr, best = 0, 0
    for i in range(len(results)):
        if curr == 0:
            curr += 1
            continue
        if results[i - 1] == results[i] - 1:
            curr += 1
        else:
            best = max(best, curr)
            curr = 0
    best = max(best, curr)
    return best

def find_best_digits():
    a, b, c, d, best = 1, 2, 3, 4, 28
    for i in range(10):
        for j in range(i + 1, 10):
            for k in range(j + 1, 10):
                for l in range(k + 1, 10):
                    curr = generate_expressions(i, j, k, l)
                    if curr > best:
                        a, b, c, d, best = i, j, k, l, curr
    return str(a) + str(b) + str(c) + str(d)

print(find_best_digits())