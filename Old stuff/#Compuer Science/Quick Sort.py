def quicksort(items):
    if len(items) <= 1:
        return items
    else:
        pointer1 = 0
        pointer2 = len(items)-1
        while pointer1 != pointer2:
            if(items[pointer1] > items[pointer2] and pointer1 < pointer2) or (items[pointer1] < items[pointer2] and pointer1 > pointer2):
                temp = items[pointer1]
                items[pointer1] = items[pointer2]
                items[pointer2] = temp
                temp_pointer = pointer1
                pointer1 = pointer2
                pointer2 = temp_pointer
            if pointer1 < pointer2:
                pointer1 = pointer1+1
            else:
                pointer1 = pointer1-1

        left = quicksort(items[0:pointer1])
        right = quicksort(items[pointer1+1:len(items)])
        return left+[items[pointer1]]+right



if __name__=="__main__":
    list = [1,34,8,5,32,7,43,56,123,57,96,21,2,4,2,3,5,15,6,65]
    print(quicksort(list))

