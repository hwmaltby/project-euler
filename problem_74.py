#Henry Maltby 2017

def evaluate_digit_factorial(n):
    facts = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    total, i = 0, 0
    while i < len(str(n)):
        total += facts[int(str(n)[i])]
        i += 1
    return total

def digit_factorial_chains():
    non_repeating_length = [0] * 2177282
    non_repeating_length[1] = non_repeating_length[2] =\
        non_repeating_length[145] = non_repeating_length[40585] = 1
    non_repeating_length[871] = non_repeating_length[872] =\
        non_repeating_length[45361] = non_repeating_length[45362] = 2
    non_repeating_length[169] = non_repeating_length[363601] =\
        non_repeating_length[1454] = 3
    total, maxl = 3, 3
    for i in range(1000000):
        if non_repeating_length[i] == 0:
            d, path = evaluate_digit_factorial(i), [i]
            while non_repeating_length[d] == 0:
                path.append(d)
                d = evaluate_digit_factorial(d)
            ans = non_repeating_length[d]
            path = path[::-1]
            for j in range(len(path)):
                non_repeating_length[path[j]] = ans + j + 1
            if non_repeating_length[i] > maxl:
                maxl = non_repeating_length[i]
                total = 0
            if non_repeating_length[i] == maxl:
                total += 1
    return total

print(digit_factorial_chains())