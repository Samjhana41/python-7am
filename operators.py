'''#
x= 10
y= 20

print(x+y)
print(x % y)
x= 10
y = 4
print(x>y)
print(x!=y)

x= True
y= False
print(x or y)
x= 10
y = 4
if x >y:
     print("y is large")
else:
    print("y is large")
'''

population=int(input("Enter your marks in population"))
science=int(input("Enter your marks in Science"))
maths=int(input("Enter your marks in Maths"))
social=int(input("Enter your marks in Social Studies"))
nepali=int(input("Enter your marks in Nepali"))
healthScience=int(input("Enter your marks in health"))
total=(population+science+maths+social+nepali+healthScience)/6

print("Total percentage : ", total)

if total >= 40:
    print("Passed")
    if (total >= 90):
        print("grade:A")
    elif (total <= 80 and total > 70):
        print("grade:B")
    elif (total <= 70 and total > 60):
        print("grade:C")
    else:
        print("grade:D")
else:
    print("Failed")

