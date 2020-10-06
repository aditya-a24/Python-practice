arr=[]
n=int(input("enter how many number you want in array : "))
for i in range(0, n):
    print("enter your", i+1, "element : ")
    ele=int(input())
    arr.append(ele)
print("here is your array : ", arr)

prod=1
for i in range(0, n):
    prod=prod*arr[i]
print("product of all elements of array is : ", prod)

no=int(input("enter number from which you want to divide : "))
ans = prod % no
print("remainder of array multiplication divided by", no, "is", ans)
