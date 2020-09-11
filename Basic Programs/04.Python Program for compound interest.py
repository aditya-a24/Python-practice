p=int(input("enter the princple amount : "))
r=float(input("enter the rate percentage : "))
t=int(input("enter time : "))
a=p*pow((1+r/100), t)
print("the amount is : ", a)
ci=a-p
print("the compound interest is : ", ci)

#using function

def ci(p, r, t):
    a=p*pow((1+r/100), t)
    return a
p=int(input("enter the princple amount : "))
r=float(input("enter the rate percentage : "))
t=int(input("enter time : "))
a=ci(p, r, t)
print("Compound interest is", a-p)