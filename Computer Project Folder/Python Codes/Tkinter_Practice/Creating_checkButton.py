from tkinter import *


def display():
    if x.get()==1:
        print("You have ticked the box")
    else:
        print("You have unticked the box")

window = Tk()

x = IntVar()
check_button = Checkbutton(window,
                           text="Tick the box",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=("Comic sans",30),
                           fg="grey",bg="black",
                           activeforeground="black",activebackground="grey",
                           padx=20,pady=20) # Pad x and y doesn't necessarily just move it to the right or left
                                            # It moves the text equidistant from the centre
check_button.pack()



window.mainloop()