"""
It must contain lower case character
It must contain upper case character
It must contain numbers
It must contain punctuation
It must be  9 to 15 characters long
"""

import string
import random

def decideLength():
    length = random.randint(9,15)
    return length

def getType(length):
    typeList = []
    allFormat = False
    while allFormat == False:
        for i in range(length):
            char = random.randint(1,4)
            typeList.append(char)
        if 1 in typeList and 2 in typeList and 3 in typeList and 4 in typeList:
            allFormat = True
    return typeList

def getLowercase(lowercaseLetters):
    return random.choice(lowercaseLetters)

def getUppercase(uppercaseLetters):
    return random.choice(uppercaseLetters)

def getDigit(numbers):
    return random.choice(numbers)

def getPunctuation(punctuation):
    return random.choice(punctuation)

def main():
    lowercaseLetters = list(string.ascii_lowercase)
    uppercaseLetters = list(string.ascii_uppercase)
    numbers = list(string.digits)
    punctuation = list(string.punctuation)
    passList = []
    typeList = getType(decideLength())
    
    for type in typeList:
        if type == 1:
            passList.append(getLowercase(lowercaseLetters))
        elif type == 2:
            passList.append(getUppercase(uppercaseLetters))
        elif type == 3:
            passList.append(getDigit(numbers))
        else:
            passList.append(getPunctuation(punctuation))
    password = ''.join(passList)
    print(password)

for i in range(100):
    main()
