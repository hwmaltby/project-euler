#Henry Maltby 2017

def where_is(n, lst):
    """
    Returns the lowest index where n could be inserted in a sorted list.
    """
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return 0 if lst[0] >= n else 1
    k = int(len(lst) / 2)
    if lst[k] >= n:
        return where_is(n, lst[:k])
    return k + 1 + where_is(n, lst[k+1:])

def equal_to_digit_factorial(n):
    facts = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    total, i = 0, 0
    while total <= n and i < len(str(n)):
        total += facts[int(str(n)[i])]
        i += 1
    if total == n:
        return True
    return False

def find_digit_factorials(n):
    total = 0
    for i in range(10, n):
        if equal_to_digit_factorial(i):
            total += i
    return total

N = 362880 * 6
print(find_digit_factorials(N))