#using while loop

n=int(input("enter any number : "))
fact=1
i=1
while i<=n:
    fact=fact*i
    i += 1
print("the factorial of {} is {}" .format(n ,fact))


#using for loop

n=int(input("enter any number : "))
fact=1
for i in range(1, n+1):
    fact=fact*i
print("the factorial of {} is {}" .format(n, fact))


#using function

def fact(n):
    temp = 1
    for i in range(1, n + 1):
        temp = temp * i
    return temp
no=int(input("enter any number : "))
print("the factorial of {} is {}" .format(no, fact(no)))


#using recursive function

def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n * (fact(n - 1))

no=int(input("enter any number : "))
print("the factorial of {} is {}" .format(no, fact(no)))