#Henry Maltby 2017

def read_roman_numeral(s):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev = 1000
    total = 0
    for c in s:
        curr = values[c]
        if prev < curr:
            total -= 2 * prev
        total += curr
        prev = curr
    return total

def make_roman_numeral(n):
    values = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII',\
        8: 'VIII', 9: 'IX', 0: ''}
    top, n = divmod(n, 1000)
    if top != 0:
        return 'M' * top + make_roman_numeral(n)
    middle, n = divmod(n, 100)
    if middle != 0:
        return values[middle].replace('I', 'C').replace('V', 'D').replace('X',\
            'M') + make_roman_numeral(n)
    lower, n = divmod(n, 10)
    if lower != 0:
        return values[lower].replace('X', 'C').replace('I', 'X').replace('V',\
            'L') + make_roman_numeral(n)
    return values[n]

def letters_saved():
    """
    """
    f = open('problem_89_roman.txt')
    total = 0
    for line in f.readlines():
        rom = line.strip()
        new_rom = make_roman_numeral(read_roman_numeral(rom))
        total += len(rom) - len(new_rom)
    return total

print(letters_saved())