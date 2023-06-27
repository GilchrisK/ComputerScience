#useful for project:    -press any key to start
                        #-press x to start
from tkinter import *

def doSomething(event):
    print("You pressed: "+event.keysym)
    # label.config(text=event.keysym) #this will show the letter on the window


window = Tk()

window.bind("<Key>",doSomething)    #window.bind  = this takes an event and a function and performs the function when the event is done
                                    #"< >" put any letter/key in this for it to be displayed

label = Label(window, font=("Helvetica",100))
label.pack()






window.mainloop()