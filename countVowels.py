vLetters = []
cLetters = []

def lowerize(letter):
    return letter.lower()


def isItVowel(letter):
    vowels = ["a", "e", "i", "o", "u"]
    if letter in vowels:
        vLetters.append(letter)
    else:
        cLetters.append(letter)

def turnListToString(list):
    strs = ""
    return strs.join(list)

def main(sentence):
    for letter in sentence:
        letter = lowerize(letter)
        if letter.isalpha():
            isItVowel(letter)

main("FIl, hakika")
print("There are " + str(len(vLetters)) + " vowels which are " + turnListToString(vLetters) + " and there are " + str(len(cLetters)) + " consonants. Which are " + turnListToString(cLetters))

