input = ("AAAABBBCCDAA")
shadowInput = input
mainList = []
dictionaryOfLetters = {}
distinctLetter = []


#count letters till they are same
def countFirstLetterOccurence(shadowInput):
    counter = 1
    for i in range(len(shadowInput)-1):
        if shadowInput[i] == shadowInput[i+1]:
            counter += 1
        else:
            break
    return counter

#log in to dictionary, key is letter, value is amount
def enterIntoDict (line, counter):
    dictionaryOfLetters[line] = counter
    

#remove counted letter from string
def removeLetterFromShadow(shadowInput, counter):
    return shadowInput[counter:]

#print dictionary
def enterDictionary(shadowInput):
    line = 1
    while shadowInput != "":
        counter = countFirstLetterOccurence(shadowInput)
        enterIntoDict(line, counter)
        line += 1
        shadowInput = removeLetterFromShadow(shadowInput, counter)
    return dictionaryOfLetters

#remove multiple occurences
def removeMultiples(input):
    for letter in input:
        if letter == input[-1]:
            continue
        