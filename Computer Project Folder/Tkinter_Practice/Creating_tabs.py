from tkinter import *
from tkinter import ttk #module that contains several different widgets such as the notebook widget

def adminPage():
    adminWindow = Tk()
    window.destroy()


window = Tk()
window.geometry("800x600")
window.config(bg="#bad7e7",pady=20)

notebook = ttk.Notebook(window) #A widget that manages a collection of windows/displays

tab1 = Frame(notebook)  #This will be a a new frame for tab1
tab2 = Frame(notebook)  #New frame for tab2

notebook.add(tab1,text="                                  Log in                                ")
notebook.add(tab2,text="                               Sign Up                                 ")
notebook.pack(pady=100)  #This will expand to fill any space
                                        #fill= will fill sapce on the x and y axis

label1 = Label(tab1,text="This is tab1",width=70,height=60)
label1.pack()
label2 = Label(tab2,text="This is tab2",width=70,height=60)
label2.pack()

button1 = Button(tab1,text="Admin",width=20,height=5,command=adminPage)
button1.pack()



window.mainloop()