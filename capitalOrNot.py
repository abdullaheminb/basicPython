capitalLetters = []
def checkCapital(letter):
    return letter.isupper()

def capital_indexes (strs):
    counter = 0
    for letter in strs:
        if checkCapital(letter):
            capitalLetters.append(counter)
        counter += 1
    return capitalLetters

print(capital_indexes("HeLLo")) 

