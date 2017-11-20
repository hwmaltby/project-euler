#Henry Maltby 22

def alpha_value(word):
    ans = 0
    for c in word:
        ans += ord(c) - 64
    return ans

def names_scores(names):
    names.sort()
    n = len(names)
    total = 0
    for i in range(n):
        total += (i + 1) * alpha_value(names[i])
    return total

f = open('problem_22_names.txt')
print(names_scores([name.strip('"') for name in f.read().split(',')]))