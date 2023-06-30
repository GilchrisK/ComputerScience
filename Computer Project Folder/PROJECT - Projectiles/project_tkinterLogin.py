from tkinter import *
from tkinter import ttk #module that contains several different widgets such as the notebook widget





def back():
    adminPage.destroy()
    starter_Window()

def switch_signUp():
    notebook.select(tab_id=signUp_tab)

def adminPage():
    adminWindow = Tk()
    adminWindow.geometry("500x400")
    starter_Window.destroy()

    # adminLogin_lbl = Label(adminWindow,text="Login")
    # adminLogin_lbl.pack(side=LEFT)
    #
    # adminEntry_Username = Entry(adminWindow,
    #                             font=("Comic sans", 35),
    #                             show="*",
    #                            )
    #
    # adminEntry_Username.pack()
    #
    # adminPassword_lbl = Label(adminWindow, text="Password")
    # adminPassword_lbl.pack(side=LEFT)
    #
    # adminEntry_Password = Entry(adminWindow,
    #                             font=("Comic sans", 35),
    #                             show="*",
    #                             )

    titleLabel = Label(adminWindow, text=" Please enter your login details... ")
    titleLabel.grid(row=0, column=0, columnspan=3, sticky="SNEW", pady=10, padx=10)

    adminLogin_lbl = Label(adminWindow, text="Username")
    adminLogin_lbl.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    adminEntry_Username = Entry(adminWindow, width="30")
    adminEntry_Username.grid(row=1, column=1, padx=10, pady=10, sticky="E")

    adminPassword_lbl = Label(adminWindow, text="Password")
    adminPassword_lbl.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    adminEntry_Password = Entry(adminWindow, width="30")
    adminEntry_Password.grid(row=2, column=1, padx=10, pady=10, sticky="E")

    backButton = Button(adminWindow, text="Back", command=lambda: back(adminWindow))
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)



    # adminEntry_Password.pack()




starter_Window = Tk()
starter_Window.geometry("1000x800")
starter_Window.minsize(1000,800)
starter_Window.config(bg="#bad7e7",padx=100,pady=150,relief=SUNKEN)
#bad7e7


notebook = ttk.Notebook(starter_Window) #A widget that manages a collection of windows/displays

# frame = Frame(notebook,relief=SUNKEN) #With 'bd=' you can vary the size of the border
# frame.place(x=100,y=0)


login_tab = Frame(notebook, padx=100)  #This will be a a new frame for tab1
signUp_tab = Frame(notebook, padx=100)  #New frame for tab2

notebook.add(login_tab, text="Log in")
notebook.add(signUp_tab, text="Sign Up")
notebook.pack()  #This will expand to fill any space

# notebook.config(height=notebook.size())               #fill= will fill space on the x and y-axis

login_lbl1 = Label(login_tab, text="Welcome back!", font=("Comic Sans", 20), width=15, height=2, anchor='center', bg="light grey")
login_lbl1.pack(pady=60)
login_lbl2 = Label(login_tab, text="Choose the account to login with :)", font=("Comic sans", 20), bg="light grey")
login_lbl2.place(x=30, y=160)

signUp_lbl1 = Label(signUp_tab, text="This is tab2", width=70, height=60)
signUp_lbl1.pack()

admin_btn = Button(login_tab, text="Admin", width=20, height=5, command=adminPage, bg="light grey")
admin_btn.place(x=100,y=300)

student_btn = Button(login_tab, text="Student", width=20, height=5, command=adminPage, bg="light grey")
student_btn.place(x=250,y=300)

signUp_btn = Button(login_tab, text="Sign Up", width=10, height=1, command=switch_signUp)
signUp_btn.place(x=330,y=420)

login_lbl3 = Label(login_tab, text="Dont have an account? Click here...", font=("Comic Sans", 11))
login_lbl3.place(x=80,y=425)
###########################








starter_Window.mainloop()

















































