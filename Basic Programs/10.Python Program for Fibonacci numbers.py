n=int(input("enter how many fibonnaci number you wants to print : "))
a=0
b=1
print("Fibonnaci series upto", n,"-th numbers : ")
for i in range(n):
    print(a, end=" ")
    c=a+b
    a=b
    b=c