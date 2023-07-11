from tkinter import *
from tkinter import ttk #module that contains several different widgets such as the notebook widget




def back(xy):
    xy.destroy()
    starter_page()
#
def starter_page():
    global starter_Window
    starter_Window = Tk()
    starter_Window.geometry("1000x800")
    starter_Window.minsize(1000,800)
    starter_Window.config(bg="#bad7e7",padx=100,pady=150,relief=SUNKEN)
    #bad7e7

    global notebook
    notebook = ttk.Notebook(starter_Window) #A widget that manages a collection of windows/displays

    # frame = Frame(notebook,relief=SUNKEN) #With 'bd=' you can vary the size of the border
    # frame.place(x=100,y=0)

    global guest_tab
    login_tab = Frame(notebook, padx=100)  #This will be a a new frame for tab1
    guest_tab = Frame(notebook, padx=100)  #New frame for tab2

    notebook.add(login_tab, text="Log in")
    notebook.add(guest_tab, text="Guest")
    notebook.pack()  #This will expand to fill any space

    # notebook.config(height=notebook.size())               #fill= will fill space on the x and y-axis

    login_lbl1 = Label(login_tab, text="Welcome back!", font=("Comic Sans", 20), width=15, height=2, anchor='center', bg="light grey")
    login_lbl1.pack(pady=60)
    login_lbl2 = Label(login_tab, text="Choose the account to login with :)", font=("Comic sans", 20), bg="light grey")
    login_lbl2.place(x=30, y=160)

    guest_lbl1 = Label(guest_tab, text="Guest account", width=70, height=60)
    guest_lbl1.pack()

    admin_btn = Button(login_tab, text="Admin", width=20, height=5,command=lambda: adminPage(login_tab), bg="light grey")
    admin_btn.place(x=100,y=300)

    student_btn = Button(login_tab, text="Student", width=20, height=5, command=lambda: studentPage(login_tab), bg="light grey")
    student_btn.place(x=250,y=300)

    guest_btn = Button(login_tab, text="Guest", width=10, height=1, command=switch_signUp)
    guest_btn.place(x=330,y=420)

    login_lbl3 = Label(login_tab, text="Click here to use a guest account...", font=("Comic Sans", 11))
    login_lbl3.place(x=78,y=423)
    ###########################

    mainloop()
######################################


def admin_submit():
    global adminMainPage


    User = adminEntry_Username.get()
    Pass = adminEntry_Password.get()
    if User != "a" or Pass != "a":
        print("The Admin username or password is incorrect...please try again")

    else:
        print("Opening admin main page")
        adminMainPage = Tk()
        adminMainPage.geometry("500x400")
        adminMainPage.minsize(800,650)
        adminWindow.destroy()
        # adminMainPage.config(bg="#bad7e7", pady=20)
        notebook = ttk.Notebook(adminMainPage,width=600,height=600)  # A widget that manages a collection of windows/displays

        createAccount_tab = Frame(notebook)     #This will be a new frame for tab1
        deleteAccount_tab = Frame(notebook)     #tab2
        changePassword_tab = Frame(notebook)    #tab3

        notebook.add(createAccount_tab, text="Create Account")
        notebook.add(deleteAccount_tab, text="Delete Account")
        notebook.add(changePassword_tab, text="Change Password")
        notebook.pack()

        crt_acc_title = Label(createAccount_tab, text="Create a student account!", width=70, height=60)
        crt_acc_title.place(x=60,y=-350)
        dlt_acc_title = Label(deleteAccount_tab, text="Delete a student account!", width=70, height=60)
        dlt_acc_title.place(x=60,y=-350)
        chng_acc_title = Label(changePassword_tab, text="Change password", width=70, height=60)
        chng_acc_title.place(x=60,y=-350)


        crt_userLbl = Label(createAccount_tab, text="Username",font=("Comic Sans",18))
        crt_userLbl.place(x=55,y=200)

        crt_userEntry = Entry(createAccount_tab, width="30")
        crt_userEntry.place(x=200,y=205)

        crt_passwordLbl = Label(createAccount_tab, text="Password",font=("Comic Sans",18))
        crt_passwordLbl.place(x=55,y=250)

        crt_passEntry = Entry(createAccount_tab, width="30",show="*")
        crt_passEntry.place(x=200,y=255)

        crt_reTypePasswordLbl = Label(createAccount_tab, text="Re-type password", font=("Comic Sans", 18))
        crt_reTypePasswordLbl.place(x=55, y=300)

        crt_reTypePasswordLbl = Entry(createAccount_tab, width="30", show="*")
        crt_reTypePasswordLbl.place(x=260, y=305)

        crt_submitButton = Button(createAccount_tab, text="Login", width=5, font=("Comic sans", 10))
        crt_submitButton.place(x=200,y=350)


        # backButton = Button(adminMainPage, text="Back", command=back)
        # backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)



################################
def switch_signUp():
    notebook.select(tab_id=guest_tab)



#################################
def studentPage(y):
    starter_Window.destroy()
    studentWindow = Tk()
    studentWindow.geometry("500x400")


    titleLabel = Label(studentWindow, text=" Please enter your login details... ")
    titleLabel.grid(row=0, column=0, columnspan=3, sticky="SNEW", pady=10, padx=10)

    studentLogin_lbl = Label(studentWindow, text="Username")
    studentLogin_lbl.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    studentEntry_Username = Entry(studentWindow, width="30")
    studentEntry_Username.grid(row=1, column=1, padx=10, pady=10, sticky="E")

    studentPassword_lbl = Label(studentWindow, text="Password")
    studentPassword_lbl.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    studentEntry_Password = Entry(studentWindow, width="30",
                                show="*")
    studentEntry_Password.grid(row=2, column=1, padx=10, pady=10, sticky="E")

    backButton = Button(studentWindow, text="Back", command=lambda: back(studentWindow))
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)


#####################################
def adminPage(x):
    global adminEntry_Username
    global adminEntry_Password
    global adminWindow
    global admin_submit
    starter_Window.destroy()
    adminWindow = Tk()
    adminWindow.geometry("500x400")


    titleLabel = Label(adminWindow, text=" Please enter your login details... ")
    titleLabel.grid(row=0, column=0, columnspan=3, sticky="SNEW", pady=10, padx=10)

    adminLogin_lbl = Label(adminWindow, text="Username")
    adminLogin_lbl.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    adminEntry_Username = Entry(adminWindow, width="30")
    adminEntry_Username.grid(row=1, column=1, padx=10, pady=10, sticky="E")

    adminPassword_lbl = Label(adminWindow, text="Password")
    adminPassword_lbl.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    adminEntry_Password = Entry(adminWindow, width="30",
                                show="*")
    adminEntry_Password.grid(row=2, column=1, padx=10, pady=10, sticky="E")

    backButton = Button(adminWindow, text="Back", command=lambda: back(adminWindow))
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)

    submitButton = Button(adminWindow,text="Login",width=5,font=("Comic sans",10),command=admin_submit)
    submitButton.grid()



starter_page()
