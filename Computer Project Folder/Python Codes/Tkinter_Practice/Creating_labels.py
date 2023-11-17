from tkinter import *

window = Tk() #creates an instance of a window

# photo = PhotoImage(file="tree.png") ##PHOTO IMPLEMENTATION DID NOT WORK

label = Label(window,text="Hello World!", font=("Arial", 40, "bold"), fg="green", bg="black")
                                                                    # fg is the colour of the writing, bg is the colour of the background of the writing
label.pack()

window.mainloop()