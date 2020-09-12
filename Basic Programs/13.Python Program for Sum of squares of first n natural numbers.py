n=int(input("enter the value of n : "))
sum=0
for i in range(1, n+1):
    sum=sum+(i**2)
print("sum of squares of first", n, "natural number is : ", sum)