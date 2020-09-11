def armstrong(n):
    temp = n
    len = count(n)
    sum=0
    while n != 0:
        r = n % 10
        sum = sum+(r**len)
        n = n//10
    return sum==temp

def count(n):
    l=0
    while n!=0:
       l += 1
       n = n // 10
    return l

n=int(input("enter any number : "))
arm=armstrong(n)
if arm is True:
    print(n, "is an armstrong number")
else:
    print(n ,"ia not an armstrong number")
