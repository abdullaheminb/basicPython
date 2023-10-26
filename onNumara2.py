import random

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

def main():
    userNumbers = getNumbers()
    winningNumbers = luckyNumbers() 
    counter = isWinner(winningNumbers, userNumbers)
    if counter >= 6 or counter == 0:
        print("You won")
        return True
    else: 
        print("You lose")
        return False

counter = 0
for i in range(100000):
    win = main()
    if win: 
        counter += 1
print(f"you won {counter} times")