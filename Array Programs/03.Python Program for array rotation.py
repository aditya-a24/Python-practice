
l=[]
n=int(input("how many elements you want to insert in array: "))
for i in range(0, n):
    print("enter your", i+1,"elements: ")
    ele=int(input())
    l.append(ele)
print("here is your list: ",l)

r=int(input("how many times you want to rotate the array: "))
print("after rotation of list by", r, "digit, here is your list: ")
for i in range(0, r):
    temp = l[0]
    for j in range(0,n-1):
        l[j] = l[j+1]
    l[n-1]=temp
print(l)