# 1.addition of two numbers
'''
a=int(input("enter your first number : "))
b=int(input("enter your ssecond numbers : "))
sum=a+b
print("the sum of",a,"and",b,"is",sum)
'''

# 2.area of circle
'''
r=float(input("enter the radius of circle: "))
ar=3.14*r**2
print("the area of circle is:", ar) 

#same code in one line

print("the area of circle is:",3.14*float(input("enter the radius of circle: "))**2)
'''

# 3.code to calculate simple interest
'''
p=float(input("enter the value of principal : "))
r=float(input("enter the rate : "))
t=int(input("enter the time : "))
si=(p*r*t)/100
print("the simple interest of given data is : ",si)
'''

# 4.code to calculate volume of cuboid
'''
l,b,h=float(input("enter the value of length : ")), float(input("enter the value of breadth : ")), float(input("enter the value of height : "))
print("the volume of cuboid is : ", l*b*h)
'''

# 5.Python script to check a number Even or Odd
'''
no=int(input("Enter any number : "))
print(no,"is an even number") if (no%2==0) else print(no, "is an odd number")
'''

# 6.Python Program to check divisibility of a number by 5
'''
no=int(input("Enter any number : "))
print(no,"is divisible by 5") if (no%5==0) else print(no, "is not divisible by 5")
'''

# 7.Python script to check for positive,negative and zero
'''
no=float(input("Enter any number : "))
if no>0:
    print(no,"is a positive number")
elif no==0:
    print("you enter zero")
else :
    print(no,"is a negative number")

#same code in one line

print(no, "is a positive number")if no>0 else print("you enter zero") if no==0 else print(no,"is a negative number")
'''

# 8.To find greatest among three numbers
'''
no1, no2, no3=int(input("enter first number : ")), int(input("enter second number : ")), int(input("enter third number : "))
if no1>no2:
    if no1>no3:
        print(no1, "is greatest number")
    elif no3>no1:
        print(no3, "is greatest number")

else :
    if no2>no3:
        print(no2, "is greatest number")
    elif no3>no2:
        print(no3, "is greatest number")

# OR

if no1>no2 and no1>no3:
    print(no1, "is greatest number")
elif no2>no1 and no2>no3:
    print(no2, "is greatest number")
else:
    print(no3, "is greatest number")
'''

# 9.Python script to check leap year
'''
year=int(input("enter any year : "))
result=("leap year")if year%400==0 else print("leap year") if year%4==0 and year%100!=0 else print("not leap year")
print(result)
'''

# 10.Python script to display number of days in a given month
'''
month=input("enter the name of any month : ")
if month=="january" or month=="march" or month=="may" or month=="july" or month=="august" or month=="october" or month=="december":
    print("31 days")
elif month=="february":
    print("28 or 29 days")
elif month=="april" or month=="june" or month=="september" or month=="november":
    print('30 days')
else :
    print("you enter wrong month")
'''

# 11.Python script to find roots of a given quadratic equation
'''
import math

a, b, c=float(input("enter the value of a : ")), float(input("enter the value od b : ")), float(input("enter the value of c : "))
discriminant=b**2-4*a*c
if discriminant>=0:
    x1=(-b+math.sqrt(discriminant))/2*a
    x2=(-b-math.sqrt(discriminant))/2*a
else:
    x1= complex((-b/(2*a)), math.sqrt(-discriminant)/(2*a))
    x2= complex((-b/(2*a)), -math.sqrt(-discriminant)/(2*a))

if discriminant > 0:
    print("The function has two distinct real roots: {} and {}".format(x1,x2))
elif discriminant == 0:
    print("The function has one double root: ", x1)
else:
    print("The function has two complex (conjugate) roots: {}  and {}".format(x1,x2))
'''

# 12.Arrange three words in dictionary order
'''
print("Enter any three words")
a, b, c=input("enter first word : "), input("enter second word : "), input("enter third word : ")
if (a<b<c):
    print(a, b, c)
elif (a<c<b):
    print(a, c, b)
elif (c<a<b):
    print(c, a, b)
elif (c<b<a):
    print(c, b, a)
elif (b<a<c):
    print(b, a, c)
elif (b<c<a):
    print(b, c, a)
'''

# 13. Python program to marksheet

print("enter the marks of all fives subjects")
a, b, c, d, e = int(input("enter the marks of 1st subject : ")), int(input("enter the marks of 2nd subject : ")), int(input("enter the marks of 3rd subject : ")), int(input("enter the marks of 4th subject : ")), int(input("enter the marks of 5th subject : "))
if a>=33 and b>=33 and c>=33 and d>=33 and e>=33 :
    print("you are pass")
    per=(a+b+c+d+e)/5
    print("you got ", per,"%")
    if per>=90:
        print("and 1st division with destinction")
    elif per>=60:
        print("and 1st division")
    elif per>=50:
        print("and 2nd division")
    else :
        print("and 3rd division")
else :
    print("You are fail")