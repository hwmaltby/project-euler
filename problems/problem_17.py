#Henry Maltby 2017

def count_letters(n):
    """n is assumed to be <=1000. 0 is given nil length."""
    if n == 1000:
        return len('one' + 'thousand')
    if n > 99:
        q, r = divmod(n, 100)
        if r == 0:
            return count_letters(r) + len("hundred") + count_letters(q)
        return count_letters(r) + len("hundred") + len("and") + count_letters(q)
    if n > 19:
        q, r = divmod(n, 10)
        tens = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',\
        7: 'seventy', 8: 'eighty', 9: 'ninety'}
        return len(tens[q]) + count_letters(r)
    ones = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',\
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',\
    12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16:\
    'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    return len(ones[n])

def total_letters_up_to(n):
    return sum([count_letters(i) for i in range(n+1)])

N = 1000
print(total_letters_up_to(N))