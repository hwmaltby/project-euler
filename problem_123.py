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

def find_answer(n):
    prms = sieve(500000)
    for i in range(len(prms)):
        p = prms[i]
        if (2 * (i + 1) * p % (p ** 2)) > n and i % 2 == 0:
            return i + 1

N = 10 ** 10
print(find_answer(N))