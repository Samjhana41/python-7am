#print()

def interest(p,time=2,rate=0.10):
    return p*time*rate
p=float(input("enter principle amount: "))
x=interest(p)
print("rs.",x)
print("si with defaulter rate and time")
r=float(input("enter rate of interest:"))
t=float(input("enter time period:"))
y=interest(p,t,r)
print("rs", y)
print("si with mordified rate and time")