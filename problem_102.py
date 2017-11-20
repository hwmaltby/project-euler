#Henry Maltby 2017

def origin_in_triangle(point1, point2, point3):
    """
    Returns true if the origin is in the triangle determined by the
    given points. Works by choosing one point, drawing a line through
    it and the origin, and determining the intersection with the
    other edge of the triangle. Repeats with another point.
    """
    a1, b1 = point1
    a2, b2 = point2
    a3, b3 = point3
    try:
        t = (a1 * b3 - b1 * a3) / (b1 * (a2 - a3) - a1 * (b2 - b3))
        s = (a2 * b1 - b2 * a1) / (b2 * (a3 - a1) - a2 * (b3 - b1))
    except ZeroDivisionError:
        return False
    return 0 < t and t < 1 and 0 < s and s < 1

f = open("problem_102_triangles.txt")
lines = f.read().strip().split("\n")
total = 0
for line in lines:
    a1, b1, a2, b2, a3, b3 = map(int, line.split(","))
    if origin_in_triangle((a1, b1), (a2, b2), (a3, b3)):
        total += 1
print(total)