from tkinter import *


def submit():
    print("The temperature is "+str(scale.get())+" degrees") #the get function obtains the value from the scale


window = Tk()

scale = Scale(window,from_= 100,to=0, #numerical size of the scale
              length=900, #length of the scale
              orient=VERTICAL,#orientation of the scale
              font=("Comic sans",20),
              tickinterval= 5,
              troughcolor="Green")#numerical indicators on the scale (goes up in 5)
              # showvalue=0) #hides current value

scale.set(((scale["from"]-scale["to"])/2)+scale["to"]) # This will ALWAYS position the slide in the middle (USEFUL)
# Scale.set(50) ##this is a simpler way, not efficient though


scale.pack()

button = Button(window, text="submit",
                command=submit,
                )
button.pack()


window.mainloop()