size = 11
hashTable=[]
for i in range(0, size):
    hashTable.append ( " ")
    print(hashTable)

def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])
    return sum%tablesize

for n in range (4):
    s = input("enter a value ")
    slot = hash(s, size)
    hashTable[slot] = s
    print(hashTable)

f = input("where is my item? ... enter one item ")

index = hash(f, size) # find the hash value

#printing the item

if hashTable[index]!=" " and hashTable[index] == f:

    print("found at " , index)

else:

    print(f, " not in your list")







