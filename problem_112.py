#Henry Maltby 2017
#better runtime (skip long intervals of bouncy numbers) possible with
#modified algorithm (to allow some sort of binary search for perc) and
#better implementation

def is_bouncy(n):
    s = str(n)
    prev = s[0]
    dec, inc = False, False
    for i in range(len(s)):
        c = s[i]
        if int(c) < int(prev):
            dec = True
        if int(c) > int(prev):
            inc = True
        if dec and inc:
            return i
        prev = c
    return False

def find_bouncy_cutoff(perc):
    total, index = 0, 1
    while total < perc * (index - 1) or index == 1:
        if is_bouncy(index):
            #would use val returned by is_bouncy(index) here to skip
            total += 1
        index += 1
    return index - 1

print(find_bouncy_cutoff(0.99))