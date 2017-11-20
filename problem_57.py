#Henry Maltby 2017

def root_two_cont_frac(n):
    """Returns a list of all partial fractions of sqrt(2) up to n."""
    numer, denom = 1, 1
    fracs = []
    while n > 0:
        numer, denom = 2*denom + numer, denom + numer
        fracs.append((numer, denom))
        n -= 1
    return fracs

def count_larger_numers(n):
    fracs = root_two_cont_frac(n)
    total = 0
    for tup in fracs:
        if len(str(tup[0])) > len(str(tup[1])):
            total += 1
    return total

N = 1000
print(count_larger_numers(N))