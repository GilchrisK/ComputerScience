import numpy as np

items = np.random.randint(1,50,8)
print(items)

n = len(items)
swapped = True

while n > 0 and swapped == True:
    swapped = False
    n = n-1
    for index in range(0,n):
        if items[index] > items[index+1]:
            temp = items[index]
            items[index] = items[index+1]
            items[index+1]=temp
            swapped = True

print(items)