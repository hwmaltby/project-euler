#Henry Maltby 2017

def evaluate_digit_square(n):
    total, i = 0, 0
    while i < len(str(n)):
        total += int(str(n)[i]) ** 2
        i += 1
    return total

def digit_square_chains(n):
    chain = [0] * (n + 1)
    chain[1] = 1
    chain[89] = 89
    for i in range(1, n + 1):
        print(i)
        if chain[i] == 0:
            d, path = evaluate_digit_square(i), [i]
            while chain[d] == 0:
                path.append(d)
                d = evaluate_digit_square(d)
            ans = chain[d]
            path = path[::-1]
            for j in range(len(path)):
                chain[path[j]] = ans
    total = 0
    for i in chain[1:]:
        if chain[i] == 89:
            total += 1
    return total

N = 10000000
print(digit_square_chains(N))