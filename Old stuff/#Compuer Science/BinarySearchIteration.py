#BinarySearch

def binarySearch(items,search_item):

    items=[2,3,6,9]
    search_item = input("Enter the item")

    found = False
    first = 0
    last = len(items)-1 #

    while first <+last and found == False:
        midpoint=(first+last)//2
        if items[midpoint]==search_item:
            found = True
        else:
            if items[midpoint]<search_item:
                first=midpoint+1
            else:
                last=midpoint-1

    if found==True:
        print("Item found at position",midpoint)
    else:
        print("Item not found")

#     # BinarySearch
# def binarySearch_recursion(items,search_item,first,last):
#     items = ["look", "down", "up"]
#     search_item = input("Enter the item")
#
#     found = False
#     first = 0
#     last = len(items) - 1
#
#     while first < +last and found == False:
#         midpoint = (first + last) // 2
#         if items[midpoint] == search_item:
#             found = True
#         else:
#             if items[midpoint] < search_item:
#                 first = midpoint + 1
#             else:
#                 last = midpoint - 1
#
#     if found == True:
#         print("Item found at position", midpoint)
#     else:
#         print("Item not found")

print("hello")

