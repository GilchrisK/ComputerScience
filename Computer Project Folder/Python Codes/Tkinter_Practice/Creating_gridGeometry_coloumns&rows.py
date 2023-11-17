from tkinter import *

#grid() = geometry manager that organizes widgets in a table-like structure.
window = Tk()

titleLabel = Label(window,text="Enter your info", font=("Arial",30))
titleLabel.grid(row=0,column=0,columnspan=2)

firstNameLabel = Label(window,text="First name: ")
firstNameLabel.grid(row=1,column=0)

firstNameEntry = Entry(window)
firstNameEntry.grid(row=1,column=1)


lastNameLabel = Label(window,text="Last name: ")
lastNameLabel.grid(row=2,column=0)

lastNameEntry = Entry(window)
lastNameEntry.grid(row=2,column=1)


emailLabel = Label(window,text="email: ")
emailLabel.grid(row=3,column=0)

emailEntry = Entry(window)
emailEntry.grid(row=3,column=1)

submitButton = Button(window,text="Submit")
submitButton.grid(row=4,column=0,columnspan=2) #'columnspan='  means that the widget will take up x number of columns

window.mainloop()