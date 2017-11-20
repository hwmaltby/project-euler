#Henry Maltby 2017

def sieve(n):
    is_prime = [True] * n
    is_prime[0], is_prime[1] = False, False
    prms = []
    for i in range(2, n):
        if is_prime[i]:
            prms.append(i)
            for j in range(i*i, n, i):
                is_prime[j] = False
    return prms

def are_perms(lst):
    """
    Returns true if all elements of lst are numbers whose digits form
    permutations of each other.
    """
    if len(lst) < 2:
        return True
    word = [c for c in str(lst[0])]
    word.sort()
    for num in lst[1:]:
        word2 = [c for c in str(num)]
        word2.sort()
        if word != word2:
            return False
    return True

def find_cool_arith_seq():
    prms = set(sieve(10000))
    for incr in range(6, 4500, 6):
        for init in range(1001, 10000 - 2*incr, 2):
            x, y, z = init, init + incr, init + 2*incr
            if x in prms and y in prms and z in prms and are_perms([x, y, z]):
                if x != 1487:
                    return str(x) + str(y) + str(z)

print(find_cool_arith_seq())