s, e=int(input("enter the starting digit : ")), int(input("enter the end digit : "))
print("all the prime numbers between {} and {} is : " .format(s, e))
for i in range(s, e):
    if i==1:
        continue
    for j in range(2, i):
        if i%j==0:
            break
    else:
        print(i, end=" ")