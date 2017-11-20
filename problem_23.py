#Henry Maltby 2017
import math

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

def num_factors(n, k):
    if n % k == 0:
        return 1 + num_factors(n/k, k)[0], num_factors(n/k, k)[1]
    return 0, n

def factorization(n, lst=None):
    facts = {}
    nsmall = math.floor(math.sqrt(n)) + 1
    if lst == None:
        lst = sieve(nsmall)
    i = 0
    while i < len(lst) and lst[i] < math.floor(math.sqrt(n)) + 1: #should i change this to nsmall? as is, updates
        exp, n = num_factors(n, lst[i])
        if exp > 0:
            facts[lst[i]] = exp
        if n in lst or n == 1:
            break
        i += 1
    if n != 1: #due to this line, does not technically function as _prime_ factorization
        facts[n] = 1
    return facts

def sum_proper_divisors(n, prms):
    facts = factorization(n, prms)
    prod = 1
    for p in facts:
        prod *= int(round((p**(facts[p] + 1) - 1) / (p - 1)))
    return prod - n

def find_sums_of_abundant_numbers(n):
    abundant_nums = []
    abundant_sums = set()
    prms = sieve(n)
    for i in range(1, n + 1):
        if sum_proper_divisors(i, prms) > i:
            abundant_nums.append(i)
            j = 0
            while j < len(abundant_nums):
                abun_sum = abundant_nums[j] + i
                if abun_sum > n:
                    j = len(abundant_nums)
                else:
                    abundant_sums.add(abun_sum)
                j += 1
    return int((n * (n + 1) / 2) - sum(abundant_sums))

N = 28123
print(find_sums_of_abundant_numbers(N))