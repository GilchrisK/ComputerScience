from tkinter import *
from tkinter import ttk #module that contains several different widgets such as the notebook widget





def adminPage():
    adminWindow = Tk()
    starter_Window.destroy()

def switch_signUp():
    notebook.select(tab_id=tab2)


starter_Window = Tk()
starter_Window.geometry("1000x800")
starter_Window.minsize(1000,800)
starter_Window.config(bg="#bad7e7",padx=100,pady=150,relief=SUNKEN)
#bad7e7


notebook = ttk.Notebook(starter_Window) #A widget that manages a collection of windows/displays

# frame = Frame(notebook,relief=SUNKEN) #With 'bd=' you can vary the size of the border
# frame.place(x=100,y=0)


tab1 = Frame(notebook,padx=100)  #This will be a a new frame for tab1
tab2 = Frame(notebook,padx=100)  #New frame for tab2

notebook.add(tab1,text="Log in")
notebook.add(tab2,text="Sign Up")
notebook.pack()  #This will expand to fill any space

# notebook.config(height=notebook.size())               #fill= will fill space on the x and y-axis

label1 = Label(tab1,text="Welcome back!",font=("Comic Sans",20),width=15,height=2,anchor='center',bg="light grey")
label1.pack(pady=60)
label3 = Label(tab1,text="Choose the account to login with :)",font=("Comic sans",20),bg="light grey")
label3.place(x=30,y=160)

label2 = Label(tab2,text="This is tab2",width=70,height=60)
label2.pack()

admin_btn = Button(tab1,text="Admin",width=20,height=5,command=adminPage,bg="light grey")
admin_btn.place(x=100,y=300)

student_btn = Button(tab1,text="Student",width=20,height=5,command=adminPage,bg="light grey")
student_btn.place(x=250,y=300)

signUp_btn = Button(tab1,text="Sign Up",width=10,height=1,command=switch_signUp)
signUp_btn.place(x=330,y=420)

label4 = Label(tab1,text="Dont have an account? Click here...",font=("Comic Sans",11))
label4.place(x=80,y=425)



starter_Window.mainloop()

















starter_Window.mainloop()































