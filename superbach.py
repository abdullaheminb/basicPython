#Asal sayıları listele
asalSayi = [2,3,5, 7,11,13,17,19,23,29,39]
fark = 0
#inputla sayi al
#number=int(input("Enter a numvber"))
number = 44
#asalı for loopa sok
for asal in asalSayi:
    fark = number - asal
    if fark in asalSayi:
        print(fark, asal)
        break     
        
#inputtan çıkar
#sonuc listede mi