

# def submit():
#     print("This is: "+ listbox.get(listbox.curselection()))

def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))

    print("This is: ")
    for index in food:
        print(index)

# def delete():
#     listbox.delete(listbox.curselection()) #This will only allow you to delete one at a time
#     listbox.config(height=listbox.size())

def delete(): #This will allow you to delete multiple at a time
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size())
def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size()) #This will adjust the size depending on the number of items(EVEN IF ONE IS REMOVED).




from tkinter import *


window = Tk()

listbox = Listbox(window,
                  bg="grey",
                  font=("Comic sans",30),
                  selectmode=MULTIPLE) #This allows you to select multiple items at once in the listbox
listbox.pack()

listbox.insert(1,"speed")
listbox.insert(2,"velocity")
listbox.insert(3,"displacement")
listbox.insert(4,"distance")
listbox.insert(5,"acceleration")
listbox.insert(6,"time")
listbox.insert(7,"drag")
listbox.insert(8,"force")
listbox.insert(9,"mass")

listbox.config(height=listbox.size()) #This will adjust the size depending on the number of items(EVEN IF ONE IS REMOVED).


entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window,text="submit", command=submit)
submitButton.pack()

addButton = Button(window,text="add", command=add)
addButton.pack()

deleteButton = Button(window,text="delete",command=delete)
deleteButton.pack()












window.mainloop()
