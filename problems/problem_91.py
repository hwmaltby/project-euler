#Henry Maltby 2017

def is_right_triangle(x1, y1, x2, y2):
    """
    Determines whether the triangle with coordinates at (0, 0), (x1,
    y1), and (x2, y2) is a right triangle.
    """
    if x1 * x2 + y1 * y2 == 0:
        return True
    if x1 * (x2 - x1) + y1 * (y2 - y1) == 0:
        return True
    if (x1 - x2) * x2 + (y1 - y2) * y2 == 0:
        return True
    return False

def find_right_triangles(m):
    """
    Returns the number of right triangles with one vertex at the
    origin and other two vertices at lattice points with coordinates
    positive and <= m.
    """
    total = 0
    for x1 in range(m + 1):
        for y1 in range(m + 1):
            if x1 == 0 and y1 == 0:
                continue
            for x2 in range(m + 1):
                for y2 in range(m + 1):
                    if (x2 == 0 and y2 == 0) or (x2 == x1 and y2 == y1):
                        continue
                    if is_right_triangle(x1, y1, x2, y2):
                        total += 1
    return total // 2

N = 50
print(find_right_triangles(N))