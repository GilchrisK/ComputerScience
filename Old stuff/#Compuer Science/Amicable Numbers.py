#harder version
Values = int(input("Please Enter a Value: "))
print("The factors of {0} are:")
for i in range (1, Values + 1):
    if Values%i == 0:
        print("{0}" .format(i))




#simpler version
x=input("enter a number")
x=int(x)
for i in range(1, x+1):
    if x%i == 0:
        print(i)


# for i in range({i[0]}):