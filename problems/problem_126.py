#Henry Maltby 2017

def cuboid_layers(n):
    lst = [0] * (n + 1)
    bound = n // 2
    x = 1
    while 3 * x * x <= bound:
        y = x
        while 2 * x * y + y * y <= bound:
            z = y
            while x * y + x * z + y * z <= bound:
                num = 2 * (x * y + x * z + y * z)
                incr = 4 * (x + y + z)
                while num <= n:
                    lst[num] += 1
                    num += incr
                    incr += 8
                z += 1
            y += 1
        x += 1
    return lst

def find_answer(n):
    attempt = 100
    lst = []
    while n not in lst:
        lst = cuboid_layers(attempt)
        attempt *= 2
    return lst.index(n)

N = 1000
print(find_answer(N))