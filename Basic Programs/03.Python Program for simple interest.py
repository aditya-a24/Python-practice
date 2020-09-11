p = float(input("enter the principle amount : "))
r = float(input("enter rate percentage : "))
t = int(input("enter time : "))
si=(p*r*t)/100
print("simple interest = ", si)

#using function

def si(p, r, t):
    SI=(p*r*t)/100
    print("Simple Interest = ", SI)
p = float(input("enter the principle amount : "))
r = float(input("enter rate percentage : "))
t = int(input("enter time : "))
si(p, r, t)