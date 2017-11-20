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
    for p in prms:
        if n % p == 0:
            return False
    return True

def primes_with_runs(n, d):
    prms = sieve(100000)
    total = 0
    if d != 0 and d != 2 and d != 8:
        start = str(d * 1111111111)
        for i in range(10):
            gen = range(10)
            if i == 0:
                gen = range(1, 10)
            for j in gen:
                num = int(start[:i] + str(j) + start[i + 1:])
                if is_prime(num, prms):
                    #print(num)
                    total += num
        return total
    if d == 2 or d == 8:
        start = str(d * 1111111111)
        for i in range(10):
            gen = range(10)
            if i == 0:
                gen = range(1, 10)
            for j in gen:
                for i2 in range(i + 1, 10):
                    gen = range(10)
                    if i2 == 0:
                        gen = range(1, 10)
                    for j2 in gen:
                        num1 = start[:i] + str(j) + start[i + 1:]
                        num2 = int(num1[:i2] + str(j2) + num1[i2 + 1:])
                        #print(num2)
                        if is_prime(num2, prms):
                            #print(num)
                            total += num2
        return total
    for i in range(1, 10):
        for j in range(10):
            num = i * 1000000000 + j
            if is_prime(num, prms):
                #print(num)
                total += num
    return total

total = 0
for i in range(10):
    print(primes_with_runs(10, i))
    total += primes_with_runs(10, i)
print(total)