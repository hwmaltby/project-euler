#Henry Maltby 2017

def available(n):
    reach = [0] * 171
    reach[0] = 1
    for i in range(1, 21):
        for j in range(1, 4):
            reach[i * j] += 1
    reach[25] += 1
    reach[50] += 1
    for i1 in range(1, 21):
        for j1 in range(1, 4):
            for i2 in range(i1, 21):
                gen = range(1, 4)
                if i1 == i2:
                    gen = range(j1, 4)
                for j2 in gen:
                    reach[i1 * j1 + i2 * j2] += 1
            reach[i1 * j1 + 50] += 1
            reach[i1 * j1 + 25] += 1
    reach[50] += 1
    reach[75] += 1
    reach[100] += 1
    ans = [0] * 171
    for i in range(2, 41, 2):
        for j in range(i, 171):
            ans[j] += reach[j - i]
    for j in range(50, 171):
        ans[j] += reach[j - 50]
    return sum(ans[:n])

N = 100
print(available(N))