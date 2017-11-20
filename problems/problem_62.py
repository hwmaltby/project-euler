#Henry Maltby 2017

def permute(n):
    """
    Returns an integer whose prime factorization uniquely identifies
    the frequencies of each digit in n.
    """
    prms = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    prod = 1
    for c in str(n):
        prod *= prms[int(c)]
    return prod

def cubic_permutations(n):
    cubes = {}
    for i in range(1, 1000000):
        i3 = i * i * i
        digits = permute(i3)
        if digits not in cubes:
            cubes[digits] = []
        cubes[digits].append(i3)
        if len(cubes[digits]) == n:
            return cubes[digits][0]

print(cubic_permutations(5))