#Henry Maltby 2017
import math

def sum_of_totients(n):
    """Returns phi(2) + phi(3) + phi(4) + ... + phi(n)."""
    n_sqrt = math.floor(math.sqrt(n) + 1)
    tnts = [1] * (n + 1)
    minl_quo, value = math.inf, -1
    for i in range(2, n):
        if tnts[i] == 1:
            tnts[i] = i - 1
            for j in range(2, (n // i) + 1):
                if (j == 2 or tnts[j] != 1) and tnts[j * i] == 1:
                    if j % i == 0:
                        tnts[j * i] = i * tnts[j]
                    else:
                        tnts[j * i] = (i - 1) * tnts[j]
    return sum(tnts) - 2

N = 1000000
print(sum_of_totients(N))