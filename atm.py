balance = 5000
dailyLimit = 2000
correctPass = "1234"
usdRate = 28
eurRate = 30

def chooseMenu():
    menuItem = int(input(
        "Isleminizi seciniz: \n" +
        "1. Para Yatir \n" +
        "2. Para Cek \n" +
        "3. Bakiyeyi gör \n" +
        "0. Cikis \n"
        ))
    return menuItem

def main(balance, dailyLimit):
    chosenMenu = chooseMenu()
    if chosenMenu == 1:
        balance = increaseBalance(balance)
    elif chosenMenu == 2:
        balance, dailyLimit = decreaseBalance(balance, dailyLimit)
    elif chosenMenu == 3:
        checkBalance(balance)
    elif chosenMenu == 0:
        exit()
    else:
        print("Hatali giris yaptiniz Tekrar deneyiniz. \n")
    main(balance, dailyLimit)
    
def increaseBalance(balance):
    deposit = int(input("Ne kadar yatiracaksiniz? \n"))
    balance += deposit
    print("Isleminiz basariyla tamamlandi. Yeni bakiyeniz " + str(balance) + " tldir. Şimdi ne yapmak istersiniz? \n")
    return balance

def decreaseBalance(balance, dailyLimit):
    withdraw = int(input("Ne kadar cekmek istersiniz? \n"))
    if balance > 0 and withdraw < balance:
        dailyLimit -= withdraw
        if dailyLimit >= 0:
            balance -= withdraw
            print("Isleminiz basariyla tamamlandi. Yeni bakiyeniz " + str(balance) + " tldir. Simdi ne yapmak istersiniz? \n")
        else:
            print("Gunluk limiti astiniz. Isleminiz gerceklestirilemiyor. Simdi ne yapmak istersiniz? \n")
    else:
        print("Bu islemi gerceklestirecek bakiyeniz yok.")

    return balance, dailyLimit

def checkBalance(balance):
    print("Hesab bakiyeniz " + str(balance) + "tl " + str(balance/eurRate) + "euro ve " + str(balance/usdRate) + " usddir. Simdi ne yapmak istersiniz? ")
    
def exit():
    print("Bizimle calistiginiz icin tesekkur ederiz")

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

if checkPass(correctPass):
    main(balance, dailyLimit)
else: 
    print("3 defa hatalı şifre girdiniz. Hesabınız bloke edildi.")
