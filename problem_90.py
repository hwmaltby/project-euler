#Henry Maltby 2017

def check_set(nums, other):
    if 6 in nums or 9 in nums:
        nums.add(6)
        nums.add(9)
    if 6 in other or 9 in other:
        nums.add(6)
        nums.add(9)
    if not(0 in nums and 1 in other or 1 in nums and 0 in other):
        return False
    if not(0 in nums and 4 in other or 4 in nums and 0 in other):
        return False
    if not(0 in nums and 9 in other or 9 in nums and 0 in other):
        return False
    if not(1 in nums and 6 in other or 6 in nums and 1 in other):
        return False
    if not(2 in nums and 5 in other or 5 in nums and 2 in other):
        return False
    if not(3 in nums and 6 in other or 6 in nums and 3 in other):
        return False
    if not(4 in nums and 9 in other or 9 in nums and 4 in other):
        return False
    if not(8 in nums and 1 in other or 1 in nums and 8 in other):
        return False
    return True

def cube_digit_pairs():
    nums = set()
    other = set()
    nums.add(8)
    other.add(1)
    nums.add(2)
    other.add(5)
    nums.add(6)
    other.add(9)
    avail1 = {0, 1, 3, 4, 5, 9, 7}
    avail2 = {0, 2, 3, 4, 6, 7, 8}
    total = 0
    c1, c2 = 0, 0
    for i1 in avail1:
        for i2 in avail1 - {i1}:
            for i3 in avail1 - {i1, i2}:
                for j1 in avail2:
                    for j2 in avail2 - {j1}:
                        for j3 in avail2 - {j1, j2}:
                            if check_set(nums | {i1, i2, i3}, other | {j1, j2,\
                                j3}):
                                total += 1
                                if 8 in {j1, j2, j3} and 1 in {i1, i2, i3}:
                                    c1 += 1
                                if 2 in {j1, j2, j3} and 5 in {i1, i2, i3}:
                                    c2 += 1
    return total // 36 * 8 + c1 // 6 + c2 // 36 + 1

print(cube_digit_pairs())