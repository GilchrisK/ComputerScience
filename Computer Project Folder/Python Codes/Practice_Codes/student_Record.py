max = 4
name = ["Max", "Paul", "Lucas", "John", "Scott"]
searchName = input("Enter name")
found = False

for i in range(0, max):
    if name[i] == searchName:
        found = True
        record_number =str(i+1)

if __name__ == "__main__":
    if found == False:
        print("Name is not in the register")
    if found == True:
        print("Record number: "+ str(record_number))


# max = 5
# name = ["Annie", "Bob", "Charles", "Dan", "Erica", "Faisal"]
# searchName = input("Enter search name")
# found = False
# for index in range(0,max):
#     if name[index] == searchName:
#         found = True
#
#
#
# if __name__ == "__main__":
#     if found == True:
#         print("Record number: " + str(index + 1))
#     if found == False:
#         print("Search name not found")