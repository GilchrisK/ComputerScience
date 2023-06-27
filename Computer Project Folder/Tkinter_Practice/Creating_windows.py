from tkinter import *

def create_window():
    new_window = Tk()           #Toplevel() = new window 'on top' of the other windows.
                                #Tk() = new independent window
    old_window.destroy()        #close out of old window


old_window = Tk()


button = Button(old_window,text="Create new window",command=create_window)
button.pack()


old_window.mainloop()