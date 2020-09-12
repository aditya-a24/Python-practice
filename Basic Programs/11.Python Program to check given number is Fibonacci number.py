import math

def isPerfectSquare(x): 
    s = int(math.sqrt(x)) 
    return s*s == x 

def is_fibo(n):
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4) 

no=int(input("enter any number : "))
if is_fibo(no) == True:
    print(no, "is a Fibbonaci number")
else:
    print(no, "is not a Fibbonaci number")