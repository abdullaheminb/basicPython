#Write a Python function that generates the Fibonacci sequence up to the n-th number. 

def calculateNext(last1, last2):
    return last1 + last2

def fibToN(n):
    last1 = 1
    last2 = 1
    temp = 0
    print(last1)
    print(last2)

    for i in range(n):
        print(calculateNext(last1, last2))
        temp = last1
        last1 = last2
        last2 += temp 
        

fibToN(10)