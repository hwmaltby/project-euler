#Henry Maltby 2017

f = open('problem_59_cipher.txt')
enc = f.read().split(',')
#freqs = [{}, {}, {}]
#for i in range(3):
#    for c in enc[i::3]:
#        if c not in freqs[i]:
#            freqs[i][c] = 0
#        freqs[i][c] += 1
#    s = [(k, freqs[i][k]) for k in sorted(freqs[i], key=freqs[i].get, reverse=True)]
#    for tup in s:
#        print(tup)
#    print("\n")

def decrypt(msg, pwd):
    dec_msg = ''
    total = 0
    for i in range(len(msg)):
        ascii_value = int(msg[i]) ^ ord(pwd[i % len(pwd)])
        total += ascii_value
        dec_msg += chr(ascii_value)
    return total

pwd = chr(103) + chr(111) + chr(100)
print(decrypt(enc, pwd))