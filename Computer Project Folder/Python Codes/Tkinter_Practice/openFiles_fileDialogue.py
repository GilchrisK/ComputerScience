#OPENFILE is not complete

from tkinter import *
from tkinter import filedialog



def openFile():
    print(filepath = filedialog.askopenfilename())



window = Tk()


button = Button(window,text="Open",command=openFile)
button.pack()




window.mainloop()