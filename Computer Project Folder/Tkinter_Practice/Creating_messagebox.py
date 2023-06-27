from tkinter import *
from tkinter import messagebox #this will import the message box library
def click():
    # messagebox.showinfo(title="Warning!",message="Be careful...")
    # messagebox.showwarning(title="Warning!",message="You have a virus")
    # messagebox.showerror(title="Error!",message="Something went wrong")
    # messagebox.askokcancel(title="Ok,cancel",message="Work will be saved")
    if messagebox.askyesno(title="yesORno",message="Do you want to continue?"): #from this you can encrypt that if you choose yes then the window will close, if you press no then the window will be continued.
        window.quit()
    else:
        window.destroy()

window = Tk()

button = Button(window,text="click me",command=click)
button.pack()









window.mainloop()