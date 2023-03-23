import json

# person = '{"name": "Bob", "languages": ["English", "French"]}'
# person_dict = json.loads(person)
#
# print(person_dict)
# print(person_dict['languages'])

f = open("DataFile.txt", "r")
data = json.loads(f)
print(data)

























# f = open("DataFile.txt", "r")
# c = f.read(DataFile.txt)
# f.write("Hello")
#split("")         #Splits sentence into words or a paragragh into sentences
                    #  You can split by any character that you put in the brackets

#when you open a file you have to close it or it will crash
# f.close()