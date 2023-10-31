"""
İkramiye havuzunun %15i birinci kategori kazananlarina
İkramiye havuzunun %8i ikinci kategori kazananlarina;
İkramiye havuzunun %10u, üçüncü kategori kazananlarina;
İkramiye havuzunun %19u dördüncü kategori kazananlarina;
İkramiye havuzunun %20si beşinci kategori kazananlarina;
İkramiye havuzunun %28i altinci kategori kazananlarina;
"""
import random
balance = 100000
winCategory = {
    6:0,
    7:0,
    8:0,
    9:0,
    10:0,
    0:0
}

#kazanan numaraları belirle
def payToll():
    global balance
    balance -= 1
  
def pickLuckyNumbers():
    luckyNumbers = []
    for i in range(22):
        luckyNumbers.append(random.randint(1,80))
    return luckyNumbers

def pickUserNumbers():
    userNumbers = []
    for i in range(10):
        userNumbers.append(random.randint(1,80))
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
        winCategory[rightPick] +=1

def distributeEarning():
    global winCategory, balance
    print(f"Lottery has been completed. {winCategory[6]} people guessed 6 numbers correctly. And each one earned: {(0.4*0.15*100000)/winCategory[6]} lira")
    print(f"Lottery has been completed. {winCategory[7]} people guessed 6 numbers correctly. And each one earned: {(0.4*0.8*100000)/winCategory[7]} lira")
    print(f"Lottery has been completed. {winCategory[8]} people guessed 6 numbers correctly. And each one earned: {(0.4*0.10*100000)/winCategory[8]} lira")
    print(f"Lottery has been completed. {winCategory[9]} people guessed 6 numbers correctly. And each one earned: {(0.4*0.19*100000)/winCategory[9]} lira")
    print(f"Lottery has been completed. {winCategory[10]} people guessed 6 numbers correctly. And each one earned: {(0.4*0.20*100000)/winCategory[10]} lira")
    print(f"Lottery has been completed. {winCategory[0]} people guessed 6 numbers correctly. And each one earned: {(0.4*0.28*100000)/winCategory[0]} lira")

for i in range(100000):
    main()
print(winCategory)
distributeEarning()