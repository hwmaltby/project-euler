#Henry Maltby
import time
import math

def normalize(x, y):
    """Normalizes the vector <x, y>."""
    if x == 0 and y == 0:
        return False
    magnitude = math.sqrt(x * x + y * y)
    return (x / magnitude, y / magnitude)

def new_slope(a, b, h, k):
    """."""
    x, y = normalize(k, - 4 * h)
    multiplier = 2 * (a * x + b * y)
    return (a - multiplier * x, b - multiplier * y)

def new_intercept(a, b, h, k):
    """."""
    if b != 0:
        m = b / a
        x = - (2 * m * (k - m * h)) / (m * m + 4) - h
    if a != 0:
        m = a / b
        y = - (8 * m * (h - m * k)) / (4 * m * m + 1) - k
    try:
        #print("4*{}^2 + {}^2 = {}".format(x, y, 4*x*x+y*y))
        return x, y
    except NameError:
        print("Error: not all variables defined. Check a={} and b={}".format(a, b))

def solve(n):
    """."""
    a, b = normalize(1.4, -19.7)
    h, k = 1.4, -9.6
    #a, b = 0, -1
    #h, k = 0, 10
    counter = 0
    while not (abs(h) < 0.01 and k > 0) and counter < n:
        a, b = new_slope(a, b, h, k)
        h, k = new_intercept(a, b, h, k)
        counter += 1
    print("Found: ({:0.6f}, {:0.6f})".format(h, k))
    return counter

start = time.time()
N = 10 ** 5
print(solve(N))
print("Elapsed time: {:0.4f}".format(time.time() - start))

'''Not used but saved for elsewhere:
def solve_quad(a, b, c):
    """."""
    try:
        disc = math.sqrt(b * b - 4 * a * c)
    except ValueError:
        print("Error: square root of a negative number. Check a={}, b={}, and c={}".format(a, b, c))
    d, e = -b, 2*a
    return (d + disc) / e, (d - disc) / e
'''