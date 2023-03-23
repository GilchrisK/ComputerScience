# def bubble(items):
#     n = len(items)
#     swapCount = 0
#     compCount=0
#     swapped = True
#     while n > 0 and swapped == True:
#         swapped = False
#         n = n-1
#         for index in range(0,n):
#             compCount +=1
#             if items[index] > items[index+1]:
#                 swapCount +=1
#                 temp = items[index]
#                 items[index] = items[index+1]
#                 items[index+1]=temp
#                 swapped = True
#
#     return(compCount, swapCount,items)



items = [2,4,6,8,9,54,42,5,3]
print(items)

n = len(items)
for index in range(1,n):
    current = items[index]
    index2 = index
    while index > 0 and items[index2 - 1] > current:
        items[index2] = items[index - 1]
        index2 = index - 1
    items[index2] = current

print(items)





if __name__=="__main__":
    girls = ["Sophia", "Lily", "Jessica", "Isabella", "Ave", "Poppy", "Emily", "Isla", "Olivia", "Amelia"]
    print(insertion(girls))