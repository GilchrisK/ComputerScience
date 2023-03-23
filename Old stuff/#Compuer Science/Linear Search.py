def linearSearch(array,target):
    found= False
    array[0]
    while not found and array[0] <len(array):
        if array[0] ==target:
            found = True
            print(array[0])
        array[0] +=1

    if found==False:
        print("element not in the list")

