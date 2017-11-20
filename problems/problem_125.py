#Henry Maltby 2017
import math

def sum_of_squares(n):
    return (n * (n + 1) * (2 * n + 1)) // 6

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def find_answer(n):
    bound = math.ceil(math.sqrt(n)) + 1
    sq_sums = [sum_of_squares(i) for i in range(bound)]
    ans = set()
    for i in range(0, bound):
        for j in range(i + 2, bound):
            num = sq_sums[j] - sq_sums[i]
            if num > n:
                break
            if is_palindrome(num):
                ans.add(num)
    return sum(ans)

N = 10 ** 8
print(find_answer(N))