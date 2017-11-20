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

def is_prime(n, prms):
    if n in prms:
        return 1
    return 0

def is_nice_concat(a, b, prms):
    if is_prime(int(str(a) + str(b)), prms) and is_prime(int(str(b) + str(a)), prms):
        return True
    return False

def prime_pair_set():
    prms_set = set(sieve(100000000))
    prms = sieve(10000)[1:]
    nice_prms = {}
    truth_values = {}
    for p in prms:
        nice_prms[p] = set()
        for q in prms:
            val = is_nice_concat(p, q, prms_set)
            if val:
                nice_prms[p].add(q)
            truth_values[(p, q)] = val
    k = 13
    nums = [k]
    for p1 in nice_prms[k]:
        for p2 in nice_prms[p1]:
            if not truth_values[(k, p2)]:
                continue
            for p3 in nice_prms[p2]:
                if not truth_values[(k, p3)] or not truth_values[(p1, p3)]:
                    continue
                for p4 in nice_prms[p3]:
                    if truth_values[(k, p4)] and truth_values[(p1, p4)] and\
                    truth_values[(p2, p4)]:
                        return (nums + [p1, p2, p3, p4])
#    while len(nums) < n:
#        for p in tmp_prms:
#            okay = True
#            for num in nums:
#                if not is_nice_concat(p, num, set_prms):
#                    okay = False
#                    tmp_prms.remove(p)
#            if okay == True:
#                nums.append(p)
#        print(nums)
#        prms = prms[1:]
#    return nums

print(sum(prime_pair_set()))