number = int(input("Enter a 4 digit number: "))

def turnNumbertoList(shadowNumber):
    digitList = []
    for i in range(4):
        digitList.append(str(shadowNumber%10))
        shadowNumber = int(shadowNumber/10)
    return digitList

def getNumber(type, digitList):
    sortedList = []
    number0 = 0
    if type == "high":
        sortedList = sorted(digitList)
    else: 
        sortedList = sorted(digitList, reverse=True)
    for i in range(len(sortedList)):
        sortedList[i] = int(sortedList[i])
    for i in range(4):
            number0 += sortedList[i]*(10**i)
    return number0

def checkTriple(digitList):
    if (digitList[0] == digitList[1] and digitList[1] == digitList[2]) or (digitList[1] == digitList[2] and digitList[2] == digitList[3]):
        return True
    else:
        return False

def main(number):
    digitList = []
    shadowNumber = number
    digitList = turnNumbertoList(shadowNumber)
    if checkTriple(digitList):
        return 0
    else:
        highNumber = getNumber("high", digitList)
        lowNumber = getNumber("low", digitList)
        return highNumber - lowNumber
     
def get6174(number):
    if main(number) != 0:
        while main(number)!= 6174:
            number = main(number)
        number = main(number)
        return number
    else:
         return "3 digit mistake"
    
print(get6174(number))
