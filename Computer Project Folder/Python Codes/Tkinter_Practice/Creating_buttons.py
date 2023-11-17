from tkinter import *
import time
count = 5
def click():
    global count
    print("Keep clicking me dude!")
    count-= 1
    print(count)
    if count == 0:
        print("The count has gotten to zero, window will now close!")
        time.sleep(2)
        window.destroy()



window = Tk() #creates an instance of a window


# photo = PhotoImage(file="C:\\Users\\Gilch\\OneDrive\\Pictures\\Saved Pictures\\tree.png")

button = Button(window, text="Click the button",
                command=click,
                font=("Comic Sans,",30),
                fg="Dark Green",
                bg="Grey",
                activeforeground="Dark Green", # Activeforeground/background makes it so that when you press the button, it will not change colour in that instant.
                activebackground="Grey")
                # state=DISABLED #This will de-activate the button
                # # state=ACTIVE) #This will re-activate a button


button.pack()
window.mainloop()