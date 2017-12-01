#Henry Maltby
import time
import math

def reversible(n):
    """
    Returns the number of reversible numbers less than 10 ** n. Relies on a 
    recurrence using three sequences (in addition to the desired one):
    * a_n = num {n + reverse(n) is all odd & has same length as n}
    * b_n = num {n + reverse(n) + 1 is all odd & has same length as n}
    * c_n = num {n + reverse(n) is all odd & has length one greater than n's}
    The relations between these sequences are elementary, and the desired 
    values are given by x_n = 2/3 * a_n + c_n.
    """
    a0, b0, c0, a, b, c, x = 1, 0, 0, 0, 5, 0, 0
    total = 0
    while n > 0:
        total += x
        a0, b0, c0, a, b, c = a, b, c, 30 * a0, 25 * c0, 20 * b0
        x = 2 * a // 3 + c
        n -= 1
    return total

start = time.time()
N = 9
print(reversible(N))
print("Elapsed time: {:0.4f}".format(time.time() - start))