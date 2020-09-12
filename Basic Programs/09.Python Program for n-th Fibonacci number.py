n=int(input("enter the nth number : "))
a = 0
b = 1
if n==0:
    print("the {}-th fibonnaci number is : {}" .format(n, a))
elif n==1 or n==2:
    print("the {}-th fibonnaci number is : {}" .format(n, b))
#elif n==2:
 #   print("the {}-th fibonnaci number is : {}" .format(n, b))
else:
    for i in range(2,n):
        c=a+b
        a=b
        b=c
    print("the {}-th fibonnaci number is : {}" .format(n, c))

#using function

def fibo(no):
    a=0
    b=1
    if no==0:
        return a
    elif no==1:
        return b
    else:
        for i in range(2, no):
            c=a+b
            a=b
            b=c
        return b
no=int(input("enter the n-th digit: "))
f = fibo(no)
print("the {}-th fibonnaci number is : {}" .format(no, f))