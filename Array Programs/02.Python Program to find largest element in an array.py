
l=[10, 324, 45, 90, 9808]
max=0
for i in range(len(l)):
    if l[i]>max:
        max=l[i]
print("the greatest number in list is:", max)


# taking input from user

l=[]
n=int(input("how many elements you wants: "))
print("enter", n, "elemnts in the list: ")
for i in range(0, n):
    l.append(int(input()))
print("here is your list:", l)
max=0
for i in range(n):
    if l[i]>max:
        max=l[i]
print("the greatest number in list is:", max)


#using function

def greatest(l,n):
    max=0
    for i in range(n):
        if l[i]>max:
            max=l[i]
    print("the greatest number in list is:", max)

l=[]
n=int(input("how many elements you wants: "))
print("enter", n, "elemnts in the list: ")
for i in range(0, n):
    l.append(int(input()))
print("here is your list:", l)
greatest(l,n)