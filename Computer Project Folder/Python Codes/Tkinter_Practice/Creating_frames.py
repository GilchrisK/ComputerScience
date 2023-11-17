# frame = a rectangular container used to group and hold widgets

from tkinter import *


window = Tk()
window.geometry("800x500")

frame = Frame(window,bg="dark green",bd=5,relief=SUNKEN) #With 'bd=' you can vary the size of the border
frame.place(x=100,y=0)                                #With 'relief=RAISED' you can create a 3D effect on your border

button1 = Button(frame,text="W",font=("Comic sans",25),width=3)
button1.pack(side=TOP)
button2 = Button(frame,text="A",font=("Comic sans",25),width=3)
button2.pack(side=LEFT)
button3 = Button(frame,text="S",font=("Comic sans",25),width=3)
button3.pack(side=LEFT)
button4 = Button(frame,text="D",font=("Comic sans",25),width=3)
button4.pack(side=LEFT)











window.mainloop()