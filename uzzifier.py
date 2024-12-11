

vowels = ["a","e","i","o","u","A","E","I","O","U"]

origword = input("enter a word: ")

origword2 = origword[::-1]

# original_string = "hello"
# letter_to_replace = "l"
# new_letter = "x"

# index = original_string.index(letter_to_replace)
# before = original_string[:index]
# after = original_string[index+1:]
# new_string = before + new_letter + after
# print(new_string)  # Output: "hexo"

#print(origword2)

# letterindex = 0

def vowelfinder():
    for letter in origword2:
        if letter in vowels:
            letterindex = origword2.index(letter)
            #print(letterindex)
            return letterindex

#print(f"first vowel is index: {vowelfinder()}")


suffix = "uzz"

word = list(origword2)

word.pop(vowelfinder())

#print(word)

word.insert(vowelfinder(), suffix)


wordrev = list(reversed(word))

finalword = ''.join(wordrev)

# print("\n")
# print(finalword[-2:])
# print(finalword[:-2])
# print(finalword[-3:])
# print(finalword[:-3])
# print(finalword[:-1])
# print(finalword[-1:])
# print("\n")

if finalword[-2:] == "ns":
    print(finalword[:-2])

elif finalword[-1:] == "s" or finalword[-1:] == "n":
    print(finalword[:-1])

else:
    print(finalword)

