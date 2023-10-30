"""
    Write a balance system where user spend money to play and earn money according to game won. 
    6 True Number gives 1 Lira
    7 True Number gives 2 Lira
    8 True Number gives 3 Lira
    9 True Number gives 4 Lira
    10 True Number gives 5 Lira
    0 True Number gives 10 Lira

    Every game played spends 1 lira.
"""
import random
counter = 0
balance = 100000

def payToll(balance):
    balance -= 1
    return balance

def earnMoney(counter, balance):
    if counter == 0:
        balance += 1000
    else:
        balance = (counter-5)*100
    return balance


#get numbers
def getNumbers():
    userNumbers = []
    for i in range(10):
        number = random.randint(10,99)
        if number not in userNumbers:
            userNumbers.append(number)
    return userNumbers

#pick winning numbers
def luckyNumbers():
    winningNumbers = []
    for i in range(22):
        number = random.randint(10,99)
        if number not in winningNumbers:
            winningNumbers.append(number)
    return winningNumbers

#check if won
def isWinner(winningNumbers, userNumbers):
    counter=0
    for number in userNumbers:
        if number in winningNumbers:
            counter += 1
    return counter

def main(balance):
    userNumbers = getNumbers()
    winningNumbers = luckyNumbers() 
    balance = payToll(balance)
    counter = isWinner(winningNumbers, userNumbers)
    if counter >= 6 or counter == 0:
        balance = earnMoney(counter, balance)
    return balance

for i in range(100000):
    balance= main(balance)
    
print(f"your balance is {balance} ")