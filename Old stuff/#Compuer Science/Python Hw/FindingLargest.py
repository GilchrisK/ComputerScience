def find_largest(items,largest):

    largest = list[0]
    for i in range(0,len(items)):
        if items(i) > largest:
            largest = items[i]
    return find_largest

if __name__ == "__main__":
    items = [12,35,13,50,9,100,59]
    find_largest(items)


