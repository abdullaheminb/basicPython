import random
balance = 100000
vault = balance
distributionRate = 0.4
winCategory = {
    6:[0,0.15],
    7:[0,0.08],
    8:[0,0.10],
    9:[0,0.19],
    10:[0,0.20],
    0:[0,0.28]
}

#kazanan numaraları belirle
def payToll():
    global balance
    balance -= 1
  
def pickLuckyNumbers():
    luckyNumbers = []
    while len(luckyNumbers)!= 22:
        luckyNumber = random.randint(1,80)
        if luckyNumber not in luckyNumbers:
            luckyNumbers.append(luckyNumber)
        else:
            continue
        
    return luckyNumbers

def pickUserNumbers():
    userNumbers = []
    while len(userNumbers)!= 10:
        userNumber = random.randint(1,80)
        if userNumber not in userNumbers:
            userNumbers.append(userNumber)
        else:
            continue
    return userNumbers

def getWinCategory(userNumbers, luckyNumbers):
    counter = 0
    for number in userNumbers:
        if number in luckyNumbers:
            counter += 1
    return counter

def main():
    global balance, winCategory
    payToll()
    luckyNumbers = pickLuckyNumbers()
    userNumbers = pickUserNumbers()
    rightPick = getWinCategory(userNumbers,luckyNumbers)
    if rightPick >= 6 or rightPick == 0:
        winCategory[rightPick][0] +=1

def distributeEarnings():
    global balance, winCategory, vault, distributionRate
    distributedAmount = 0
    for key in winCategory:
        if winCategory[key][0] != 0:
            print(f"{winCategory[key][0]} people guessed {key} numbers correctly. And each one earned {(vault*distributionRate*winCategory[key][1])/winCategory[key][0]} lira. ")
            distributedAmount += vault*distributionRate*winCategory[key][1]
        else:
            print(f"No one has been able to guess {key} numbers correctly. Money sent back to the vault.")
    print(f"We distributed {distributedAmount} lira from {vault} lira we had collected.")

for i in range(100000):
    main()
print(winCategory)
distributeEarnings()

