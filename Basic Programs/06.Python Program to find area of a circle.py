r=int(input("enter the value of radius : "))
pi=3.142
ar=pi*r**2
print("area of circle is : ", ar)

#using function

def ar_of_circle(r):
    pi=3.142
    ar=pi*r**2
    print("area of circle is : ", ar)

ar_of_circle(int(input("enter the value of radius : ")))