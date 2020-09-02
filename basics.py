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

l,b,h=float(input("enter ther value of length : ")), float(input("enter ther value of breadth : ")), float(input("enter ther value of height : "))
print("the volume of cuboid is : ", l*b*h)