from tkinter import *


def order():
    if x.get()==0:
        print("This is speed")
    elif x.get()==1:
        print("This is time")
    elif x.get()==2:
        print("This is distance")
    else:
        print("Huh?")

motion = ["Speed", "Time", "Distance"]

window = Tk()

x = IntVar()

for index in range(len(motion)):
    radio_button = Radiobutton(window,
                               text=motion[index], #adds text to radiobuttons
                               variable=x, #groups radiobuttons together if they share the same variable
                               value=index,#assigns each radiobutton on a different value
                               width=30,
                               command=order)


    radio_button.pack()




window.mainloop()
