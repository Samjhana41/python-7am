num=int(input("Enter number of students"))
increment = 1

while increment<=num:
    print("Hello")
    increment += 1

studentsMask = []
while increment <= num:
    print(f"=========student {increment}===========")
    for x in range (1):
        nep=float(input("Enter nepali mask: " ))
        eng= float(input("Enter english mask: "))
        math= float(input("Enter math mask: "))
        pop = float(input("Enter population mask: "))
        masks = [nep,eng,math,pop]
        studentsMask.append(masks)

        increment +=1

    print(studentsMask)
    for sMasks in studentsMask
        for sm in sMask:
            print(sm)