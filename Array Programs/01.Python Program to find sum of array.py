
a=[1, 2, 3]
s=0
for i in range(len(a)):
    s=s+a[i]
print(s)


# by taking input from user

l=[]
n=int(input("enter the numbers of elements you want in list: "))
print("enter the", n, "elements in list: ")
for i in range(0, n):
     ele=int(input())
     l.append(ele)
print("here is your list:", l)
s=0
for i in range(len(l)):
    s=s+l[i]
print("sum of", l, "is:", s)


# using function

def sum(l):
    s=0
    for i in range(len(l)):
        s=s+l[i]
    print("sum of", l, "is:", s)    

l=[]
n=int(input("enter the numbers of elements you want in list: "))
print("enter the", n, "elements in list: ")
for i in range(0, n):
     ele=int(input())
     l.append(ele)
print("here is your list:", l)
sum(l)