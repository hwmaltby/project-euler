#Henry Maltby 2017

def lattice_paths(m, n):
    m, n = max(m, n), min(m, n)
    prod = 1
    for i in range(n):
        prod *= (m + i + 1)
        prod /= (i + 1)
    return int(prod)

M, N = 20, 20
print(lattice_paths(M, N))