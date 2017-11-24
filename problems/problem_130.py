#Henry Maltby 2017

def sieve(n):
    a = [True] * (n + 1)
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            for n in range(i*i, n + 1, 2*i):
                a[n] = False

    return a

def f(n):
    #returns the smallest value of k such that 11..1 = 0 mod n, where 11..1 has k 1's
    total = 0
    start = True
    summand = 1
    i = 0
    while total != 0 or start:
        start = False
        total = (total + summand) % n
        summand = (summand * 10) % n
        i += 1
    return i

a = sieve(99999)
count = 0
total = 0
i = 1
while count < 25:
    i += 1
    if a[i] or i % 2 == 0 or i % 5 == 0:
        continue
    #print(i)
    if (i - 1) % f(i) == 0:
        count += 1
        total += i
        print(i)
        print("is good")

print(total)