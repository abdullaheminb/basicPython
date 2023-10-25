x = 13434312
tempX = x
reversed = 0       
if x == 0:
    ans = "polindrome"
elif x < 0:
    ans = "not polindrome"
else:
    while tempX>9:
        reversed += tempX%10
        reversed *= 10
        tempX -= tempX%10
        tempX = tempX/10
    reversed += tempX
    if reversed == x:
        ans = "polindrome"
    else: 
        ans = "not polindrome"
print(ans)