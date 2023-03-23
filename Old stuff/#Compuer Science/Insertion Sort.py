import numpy as np

items = np.random.randint(1,50,8)
print(items)

n = len(items)

for index in range(1,n):
    current = items[index]