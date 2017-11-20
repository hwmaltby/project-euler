#Henry Maltby 2017
import math

def is_palindrome(n):
    word = str(n)
    return (word == word[::-1])

def three_by_three():
    ans = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            k = i * j
            if is_palindrome(k):
                ans = max(k, ans)
    return ans

print(three_by_three())