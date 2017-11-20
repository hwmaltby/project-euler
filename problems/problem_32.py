#Henry Maltby 2017
import math

def all_digits(s):
    if len(s) != 9:
        return False
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for d in digits:
        if d not in s:
            return False
    return True

def pandigital():
    """Returns the sum of all pandigital products."""
    nums = set()
    for i in range(2, 10):
        upper_bound = int(math.floor(9876 / i))
        for j in range(1234, upper_bound):
            k = i * j
            if all_digits(str(i) + str(j) + str(k)):
                nums.add(k)
    for i in range(10, 99):
        upper_bound = int(math.floor(9876 / i))
        for j in range(123, upper_bound):
            k = i * j
            if all_digits(str(i) + str(j) + str(k)):
                nums.add(k)
    return sum(nums)

print(pandigital())