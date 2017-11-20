#Henry Maltby 2017

def collatz(n, dct):
    if n in dct:
        return dct[n]
    if n % 2 == 0:
        dct[n] = 1 + collatz(n/2, dct)
    else:
        dct[n] = 1 + collatz(3*n + 1, dct)
    return dct[n]

def longest_collatz_sequence(n):
    dct = {1: 0}
    key = 1
    for i in range(2, n):
        collatz(i, dct)
        if dct[i] > dct[key]:
            key = i
    return key

N = 1000000
print(longest_collatz_sequence(N))