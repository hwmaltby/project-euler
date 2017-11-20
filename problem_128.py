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

def find_tiles(n):
    prms = set(sieve(12 * n + 6))
    lst = [1]
    for i in range(1, n + 1):
        num = 3 * i * i + 3 * i + 1
        num2 = 3 * i * i - 3 * i + 2
        if 6 * i - 1 in prms and 6 * i + 1 in prms and 12 * i + 5 in prms:
            lst.append(num2)
        if 6 * i - 1 in prms and 6 * i + 5 in prms and 12 * i - 7 in prms:
            if num != 7:
                lst.append(num)
    return lst

N = 100000
print(find_tiles(N)[2000 - 1])