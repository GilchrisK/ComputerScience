from tkinter import *

def doSomething(event):
    # print("Mouse coordinates: "+ str(event.x)+","+str(event.y))
    coord.set(str(event.x)+","+str(event.y))
    window.update_idletasks()

window = Tk()

coord = StringVar

window.bind("<Button-1>",doSomething)   #left mouse click
# window.bind("<Button-2>",doSomething)   #scroll wheel
# window.bind("<Button-3>",doSomething)   #right mouse click
window.bind("<Motion>",doSomething)


coordinates = Label(window,textvariable=coord)
coordinates.pack()



window.mainloop()