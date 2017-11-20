#Henry Maltby 2017

def gcd(a, b):
    """Returns the greatest common divisor of naturals a and b."""
    if b == 0:
        return a
    a, b = max(a, b), min(a, b)
    return gcd(b, (a % b))

def simple_frac(frac):
    """Returns a fraction in lowest terms."""
    k = gcd(frac[0], frac[1])
    return [int(frac[0] / k), int(frac[1] / k)]

def does_it_simplify(a, b, c):
    q = a / b
    a = int(str(a)[str(a).index(str(c)) - 1])
    b = int(str(b)[str(b).index(str(c)) - 1])
    if q == a / b:
        return True
    return False

def find_fractions():
    """
    """
    fracs = []
    for i in range(10, 100):
        x, b = int(str(i)[0]), int(str(i)[1])
        for a in [x, b]:
            if a != 0:
                for j in range(1, 10):
                    m = 10*a + j
                    if m > i and does_it_simplify(i, m, a):
                        fracs.append([i, m])
                    m = 10*j + a
                    if m > i and does_it_simplify(i, m, a):
                        fracs.append([i, m])
    return fracs

def mult_fracs(lst):
    prod = [1, 1]
    for frac in lst:
        frac = simple_frac(frac)
        prod[0] = prod[0] * frac[0]
        prod[1] = prod[1] * frac[1]
    prod = simple_frac(prod)
    return prod

print(mult_fracs(find_fractions())[1])