#Can use this while saving a file, or it could lead to a file opening
from tkinter import *
from tkinter.ttk import *
import time

def start():
    button.destroy()
    MB = 10
    Saving =0
    speed = 1
    while Saving<MB:
        time.sleep(0.02)
        bar["value"]+=(speed/MB)*100
        Saving+=speed
        percent.set(str(int((Saving/MB)*100))+"%")
        # text.set(str(Saving)+"/"+str(MB)+" MB completed")
        text.set("Saving...") #better than the line above
        window.update_idletasks()

window = Tk()

percent = StringVar() #allows us to update percent with some new text
text = StringVar()
bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)

percentLabel = Label(window,textvariable=percent) #textvariable is used so we can update the label with text after each iteration of our while loop
percentLabel.pack()

taskLabel = Label(window,textvariable=text) #textvariable is used so we can update the label with text after each iteration of our while loop
taskLabel.pack()

button = Button(window,text="Save",command=start)
button.pack()











window.mainloop()