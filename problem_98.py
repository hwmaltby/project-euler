#Henry Maltby 2017

def good_squares():
    sqs = [str(i * i) for i in range(1, 31623)]
    #to_replace = {'1': '!', '2': '@', '3': '#', '4': '$', '5': '%', '6': '^',\
    #    '7': '&', '8': '*', '9': '(', '0': ')'}
    #for i in range(len(sqs)):
    #    for key in to_replace:
    #        sqs[i].replace(key, to_replace[key])
    key_organizer = {}
    lexicographical = {}
    for sq in sqs:
        key = "".join(sorted(list(str(sq)), key=int))
        if key not in lexicographical:
            lexicographical[key] = set()
        lexicographical[key].add(str(sq))
        coded = cipher(key)
        if coded not in key_organizer:
            key_organizer[coded] = set()
        if key not in key_organizer[coded]:
            key_organizer[coded].add(key)
    return key_organizer, lexicographical

def cipher(word):
    queue = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
    code = {}
    new_word = ""
    for c in word:
        if c not in code:
            e = queue.pop(0)
            code[c] = e
        new_word += code[c]
    return new_word

def check_equal(word1, word2):
    if len(word1) != len(word2):
        return False
    if len(word1) == 0:
        return True
    code = {}
    for i in range(len(word1)):
        if word2[i] != word1[i]:
            code[word2[i]] = word1[i]
            word2 = word2.replace(word2[i], word1[i])
    return word1 == word2, code

def find_word_pairs():
    f = open("problem_98_words.txt")
    words = [x[1:-1] for x in f.read().split(",")]
    alphabetical = {}
    for word in words:
        key = "".join(sorted(list(word), key=ord))
        if key not in alphabetical:
            alphabetical[key] = set()
        alphabetical[key].add(word)
    key_organizer, lexicographical = good_squares()
    #print(key_organizer)
    #print(lexicographical)
    maxl = 0
    for key in alphabetical:
        if len(alphabetical[key]) < 2:
            continue
        enc = cipher(key)
        if enc in key_organizer:
            for digits in key_organizer[enc]:
                if len(lexicographical[digits]) < 2:
                    continue
                #print(digits)
                count = 0
                for word1 in alphabetical[key]:
                    for word2 in alphabetical[key]:
                        for sq in lexicographical[digits]:
                            word2change = word2
                            tup = check_equal(sq, word1)
                            if tup[0]:
                                for i in tup[1]:
                                    word2change = word2change.replace(i, tup[1][i])
                                if word2change in lexicographical[digits] - {sq}:
                                    maxl = max(maxl, int(word2change))
    return maxl

print(find_word_pairs())