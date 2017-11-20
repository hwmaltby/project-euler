#Henry Maltby 2017

def partition(n, m):
    pents, i = [0], 1
    while pents[-1] < n:
        q, r = divmod(i, 2)
        if r == 1:
            q += 1
            pents.append((q * (3 * q - 1)) // 2)
        else:
            pents.append((q * (3 * q + 1)) // 2)
        i += 1
    pents = pents[1:]
    parts, num = [1], 1
    while parts[-1] % m != 0 and num < n:
        to_append = 0
        sgn, count = 1, 0
        while pents[count] <= num:
            to_append += sgn * parts[num - pents[count]]
            if count % 2 == 1:
                sgn *= -1
            count += 1
        parts.append(to_append % m)
        num += 1
    return num

N, M = 100000, 1000000
print(partition(N, M) - 1)