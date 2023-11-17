numbers = [0,0,0,0,0,0]
total = 0
for index in range(0,5):
    numbers[index] = int(input("Enter next number"))
    total = numbers[index] + total

for index in range(5,0):
    print(numbers[index])
print(total)
average = total/6
print(average)
