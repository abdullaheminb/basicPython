import random
correctPass = "1234"
balance = 50

#decideWinners
def decideWinners(winningList):
    for i in range(22):
        winningList.append(random.randint(10, 99))
    return winningList

#check menu
def seeMenu():
    menuItem = int(input(
                         "Welcome to Number 10. Play random numbers to win BIG! Choose a menu item by typing the menu number.\n"
                         "1. See Your Balance \n" 
                         "2. Deposit Money into Account\n"
                         "3. Withdraw Money\n"
                         "4. Play Game\n"
                         "5. Play for Me\n"
                         "6. Play for Me 10 Times\n"
                         "0. Exit\n"
                         ))
    return menuItem

#deposit money
def deposit(balance):
    deposit = int(input("How much you want to deposit?\n"))
    balance += deposit
    print(f"you have successfully deposited {deposit} lira into your account.\n"
          f"Your current balance is {balance}\nSending you back to menu")
    main(balance)

#withdraw money
def withdraw(balance):
    withdraw = int(input("How much you want to withdraw? \n"))
    if balance > 0 and balance > withdraw:
        balance -= withdraw
        print(f"You have successfully withdrawn. Your current balance is {balance}\nSending you back to menu\n")
    main(balance)

#check balance
def checkBalance(balance):
    print(f"Your current balance is {balance}\nSending you back to menu \n")
    main(balance)

#play game
def game(balance):
    luckyNumbers = []
    winningList = []
    decideWinners(winningList)
    for i in range(10):
        luckyNumbers.append(int(input(f"Choose your two digited lucky number {i+1}:\n")))
    print(f"you selected {luckyNumbers}\n")
    balance, toll = payToll(balance)
    if toll == True:
        result = checkResult(luckyNumbers, winningList)
        if result == 6:
            print("You correctly guessed 6 numbers. And won 1 lira")
            balance = earnMoney(1)
        elif result == 7:
            print("You correctly guessed 7 numbers. And won 2 lira")
            balance = earnMoney(2)
        elif result == 8:
            print("You correctly guessed 8 numbers. And won 3 lira")
            balance = earnMoney(3)
        elif result == 9:
            print("You correctly guessed 9 numbers. And won 4 lira")
            balance = earnMoney(4)
        elif result == 10:
            print("You correctly guessed 10 numbers. And won 5 lira.")
            balance = earnMoney(balance, 5)
        elif result == 0:
            print("You couldn't guessed any numbers. And won 10 lira")
            balance = earnMoney(10)
        else:
            print("Not lucky. \n")
        print(f"Your current balance is {balance}.")
        playAgain = int(input("Do you want to try again? \n1. Yes \n 2. No\n"))
        if playAgain == 1:
            game(balance)
        elif playAgain == 2:
            main()
        else:
            print("Thats not a viable option. Directing you to menu.")
            main()


    return luckyNumbers

#check result
def checkResult(luckyNumbers, winningList):
    correctGuess = 0
    for number in luckyNumbers:
        if number in winningList:
            correctGuess += 1
    return correctGuess

#pay toll
def payToll(balance):
    isTicketed = int(input(f"Would you like to spend 1 lira to play? \n 1.Yes \n 2.No\n"))
    if isTicketed == 1:
        balance -= 1
        return balance, True
    elif isTicketed == 2:
        print("Thanks for visiting. Directing you to menu\n")
        return balance, False
    else:
        print("Thats not a viable option. Directing you to menu")
        return False

#claim earnings
def earnMoney(balance, amount):
    balance += amount
    return balance

#main
def main(balance):
    chosenMenu = seeMenu()
    if chosenMenu == 1:
        checkBalance(balance)
    elif chosenMenu == 2:
        deposit(balance)
    elif chosenMenu == 3:
        withdraw(balance)
    elif chosenMenu == 4:
        game(balance)
    elif chosenMenu == 5:
        playForMe(balance)
    elif chosenMenu == 6:
        playForMe10(balance)
    elif chosenMenu == 0:
        print("Thanks for Playing")
    else:
        print("Thats not a viable option. Please try again.")
        main(balance)

#check password
def checkPass(correctPass):
    authorized = False
    for i in range(3):
        userPass = input("Sifrenizi giriniz")
        if userPass == correctPass:
            authorized = True
            break
        else:
            authorized = False
    return authorized

def playForMe(balance):
    luckyNumbers = []
    winningList = []
    decideWinners(winningList)
    for i in range(10):
        luckyNumbers.append(random.randint(10,99))

authorized = checkPass(correctPass)
if authorized:
    main(balance)
else:
    print("you are locked out of your account")