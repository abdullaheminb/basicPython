import random
reward={
    1:[[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36],2,"Red"],
    2:[[2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35],2,"Black"],
    3:[list(range(1,13)),3,"First 12"],
    4:[list(range(13,25)),3,"Second 12"],
    5:[list(range(25,37)),3,"Third 12"],
    6:[list(range(2,37,2)),2,"Evens"],
    7:[list(range(1,36,2)),2,"Odds"],
    8:[list(range(1,18)),2,"First 18"],
    9:[list(range(19,37)),2,"Second 18"]
    }

balance = 500 

#Get users risk amount check if balance enough
def bet():
    global balance
    if balance == 0:
        print("You are out of money. Good bye.")
        playable = 0
        risk = 0
    else:
        risk = int(input(f"Your balance is: {balance} Choose the amount you want to bet: "))
        if risk > balance:
            print("You can't bet more than you have. Try again")
            playable = 1
        else:
            playable = 2
    return risk, playable

#Get users choice
def menu():
    selection = int(input(
        """
        Rulet oyununa hosgeldiniz. Oynamak istediğiniz tarzi seciniz\n
        1. Choose Red\n
        2. Choose Black\n
        3. Choose First 12\n
        4. Choose Second 12\n
        5. Choose Third 12\n
        6. Choose Evens\n
        7. Choose Odds\n
        8. Choose First 18\n
        9. Choose Second 18\n
        0. Exit\n
        """)) 
    return selection

#Pick a lucky number
def pickWinner():
    return random.randint(1,36)

#check if users choice is in lucky number if so return multiplier
def winCondition(choice,luckyNumber):
    global reward
    print(choice)
    #choice -= 1
    if luckyNumber in reward[choice][0]:
        print(f"You have won. Because {luckyNumber} is in {reward[choice][2]} and your bet have increased {reward[choice][1]} times")
        return (reward[choice][1])
    else:
        print(f"You lost because {luckyNumber} is not in {reward[choice][2]} ")
        return 0

#update balance
def updateBalance(multiplier, risk):
    global balance
    balance += multiplier*risk

def main():
    global balance
    while 1:
        riskAmount, playable = bet()
        if playable == 0:
            break
        elif playable == 1:
            continue

        balance -= riskAmount

        choice = menu()
        if choice == 0:
            print("Tekrar bekleriz.")
            break
        elif choice not in reward.keys():
            print("Wrong Choice Try again")
            continue
        
        luckyNumber = pickWinner()
        
        balance += riskAmount * winCondition(choice, luckyNumber)
        
main()