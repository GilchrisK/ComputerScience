def divide_Algorithm(mylist):

    mylist = []
    n = len(mylist)/2
    list1 = mylist[:n]
    list2 = mylist[n:]

if __name__=="__main__":
    list1 = [2,5,8,13,15,19,23]
    list2 = [1,3,9,12,15]
    print(divide_Algorithm(mylist))

    #NOT FINISHEDDDDDDDDDDDDDD



# def merge_Algorithm(list1, list2):
#
#     p1 = 0
#     p2 = 0
#     list3 = []
#
#     while p1 < len(list1) and p2 < len(list2):
#         if list1[p1] < list2[p2]:
#             list3.append(list1[p1])
#             p1 += 1
#         else:
#             list3.append(list2[p2])
#             p2 += 1
#     if len(list1) > len(list2):
#         list3.append(list1[p1:])
#     else:
#         list3.append(list2[p2:])
#
#     return list3
#
# if __name__=="__main__":
#     list1 = [2,5,8,13,15,19,23]
#     list2 = [1,3,9,12,15]
#     print(merge_Algorithm(list1,list2))

































