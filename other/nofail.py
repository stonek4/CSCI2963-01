import sys
words = []
with open(sys.argv[1]) as input_file:
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for line in input_file:
        for word in line.split():
            if word != "":
                first = word[0]
                skip = True
                total = 0
                for letter in word:
                    if skip == True:
                        skip = False
                    else:
                        pos = 1
                        for symbol in alphabet:
                            if letter == symbol:
                                total += pos
                                break
                            pos += 1
                total -= 1
                if total < 26:
                    if first == alphabet[total]:
                        words.append(word)
print words
