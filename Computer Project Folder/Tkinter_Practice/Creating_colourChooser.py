#PROJECT, can assign colours to things
#Day and night feature in the projectiles

from tkinter import *
from tkinter import colorchooser #this is a submodule

def click():
    colour = colorchooser.askcolor()
    colourHex = colour[1]
    window.config(bg=colourHex) #This will change the background colour




window = Tk()
window.geometry("420x430")

button = Button(window,text="click me",command=click)
button.pack()










window.mainloop()