import random
balance = 500
risk = 0
def checkRisk():
    global balance, risk
    if balance == 0:
        print("Kumarda kaybettin")
        return False
    else:
        risk = int(input(f"Anlık paranız: {balance} Risk etmek istediğiniz miktar nedir: (cikis icin 0)"))
        if risk==0:
            return False
        if risk <= balance:
            balance -= risk
            return True
        else:
            return False

def youwin(multiplier):
    global balance
    balance += risk * multiplier
    print(balance)

def menu():
    secenek = int(input(
        """
        Rulet oyununa hosgeldiniz. Oynamak istediğiniz tarzı seciniz.o\n
        1. Tek sayilari sec\n
        2. Cift sayilari sec\n
        3. 1-12 yi sec\n
        4. 2-12 yi seco\n
        5. 3-12 yi seco\n
        6. Kırmızıları seco\n
        7. Siyahları Seco\n
        8. İlk 18i seco\n
        9. İkinci 18i seco\n
        0. Cikiso\n
        """)) 
    return secenek

def luckyNumber():
    winner = random.randint(1,36)
    print(f"Kazanan sayi{winner}")
    return winner



def usersCategory(winner,secenek):
    kirmizi = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
    siyah = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
    ilkOnIki = list(range(1,13))
    ikinciOnIkı = list(range(13,25))
    ucuncuOnIki = list(range(25,37))
    ciftSayilar = list(range(2,37,2))
    tekSayilar = list(range(1,36,2))
    ilkOnSekiz = list(range(1,18))
    ikinciOnSekiz = list(range(19,37))

    if secenek == 1 and winner in tekSayilar:
        print("Kazandin 2x")    
        youwin(2)    

    elif secenek == 2 and winner in ciftSayilar:
        print("Kazandin 2x")
        youwin(2)    

    elif secenek == 3 and winner in ilkOnIki:
        print("Kazandin 3x")
        youwin(3)

    elif secenek == 4 and winner in ikinciOnIkı:
        print("Kazandin 3x")
        youwin(3)
    
    elif secenek == 5 and winner in ucuncuOnIki:
        print("Kazandin 3x")
        youwin(3)
    elif secenek == 6 and winner in kirmizi:
        print("Kazandin 2x")
        youwin(2)
    
    elif secenek == 7 and winner in siyah:
        print("Kazandin 2x")
        youwin(2)

    elif secenek == 8 and winner in ilkOnSekiz:
        print("Kazandin 2x")
        youwin(2)

    elif secenek == 9 and winner in ikinciOnSekiz:
        print("Kazandin 2x")
        youwin(2)

    elif secenek == 0:
        print("Gule Gule")
    
    else:
        print("Kaybettiniz")
        
        

def main():
    global balance
    #Kullanıcıya menu goster
    while 1:
        if checkRisk():
            secenek = menu()
            winner = luckyNumber()
            categoryOfUser = usersCategory(winner,secenek)
        else:
            print("Gule gule")
            break


main()