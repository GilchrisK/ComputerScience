import project_validation
import sqlite3
import tkinter.messagebox
from tkinter import *
import tkinter as tk
from tkinter import ttk  # module that contains different widgets such as the notebook widget
# import project_saveData

# def test():
#     #create object of login()
#     object.method




def back(xy):
    xy.destroy()
    starter_page()


#
def starter_page():
    global starter_Window
    starter_Window = Tk()
    starter_Window.geometry("1000x800")
    starter_Window.minsize(1000, 800)
    starter_Window.config(bg="#bad7e7", padx=100, pady=150, relief=SUNKEN)

    global notebook
    notebook = ttk.Notebook(starter_Window)  # A widget that manages a collection of windows/displays

    global guest_tab
    login_tab = Frame(notebook, padx=100)  # This will be a new frame for tab1
    guest_tab = Frame(notebook, padx=100)  # New frame for tab2

    notebook.add(login_tab, text="Log in")
    notebook.add(guest_tab, text="Guest")
    notebook.pack()  # This will expand to fill any space

    # notebook.config(height=notebook.size())               #fill= will fill space on the x and y-axis

    login_lbl1 = Label(login_tab, text="Welcome back!", font=("Comic Sans", 20), width=15, height=2, anchor='center',
                       bg="light grey")
    login_lbl1.pack(pady=60)
    login_lbl2 = Label(login_tab, text="Choose the account to login with :)", font=("Comic sans", 20), bg="light grey")
    login_lbl2.place(x=30, y=160)

    guest_lbl1 = Label(guest_tab, text="Guest account", width=70, height=60)
    guest_lbl1.pack()

    admin_btn = Button(login_tab, text="Admin", width=20, height=5, command=lambda: adminPage(login_tab),
                       bg="light grey")
    admin_btn.place(x=100, y=300)

    student_btn = Button(login_tab, text="Student", width=20, height=5, command=lambda: studentPage(login_tab),
                         bg="light grey")
    student_btn.place(x=250, y=300)

    guest_btn = Button(login_tab, text="Guest", width=10, height=1, command=switch_signUp)
    guest_btn.place(x=330, y=420)

    login_lbl3 = Label(login_tab, text="Click here to use a guest account...", font=("Comic Sans", 11))
    login_lbl3.place(x=78, y=423)
    ###########################

    mainloop()


######################################

from tkinter import messagebox


def admin_submit():
    def connect_database(a, b, c, d):
        if a == '' or b == '' or c == '' or d == '':
            messagebox.showerror("Error", "All fields must be completed")
        elif c != d:
            messagebox.showerror("Error","Passwords do not match")
        flagA = project_validation.validate_studentEmail(a)
        flagB = project_validation.isValidUsername(b)
        flagC = project_validation.isValidPassword(c)
        if flagA and flagB and flagC:
            from project_saveData import saveMyData

            saveMyData(a,b,c)
        else:
            messagebox.showerror("Error","Invalid information")

    global adminMainPage

    User = adminEntry_Username.get()
    Pass = adminEntry_Password.get()
    if User == '' or Pass == '':
        messagebox.showerror("Error", "All fields must be completed")
    elif User != "Teacher" or Pass != "Projectiles123":
        messagebox.showerror("Error", "Invalid! The Admin username or password is incorrect")

    else:

        #Main page is now opened
        adminMainPage = Tk()
        adminMainPage.geometry("500x400")
        adminMainPage.minsize(800, 650)
        adminWindow.destroy()
        notebook = ttk.Notebook(adminMainPage, width=600,
                                height=600)  # A widget that manages a collection of windows/displays

        createAccount_tab = Frame(notebook)  # This will be a new frame for tab
        deleteAccount_tab = Frame(notebook)  # tab2
        changePassword_tab = Frame(notebook)  # tab3

        notebook.add(createAccount_tab, text="Create Account")
        notebook.add(deleteAccount_tab, text="Delete Account")
        notebook.add(changePassword_tab, text="Change Password")
        notebook.pack()

        crt_acc_title = Label(createAccount_tab, text="Create a student account!", width=70, height=60)
        crt_acc_title.place(x=60, y=-350)
        dlt_acc_title = Label(deleteAccount_tab, text="Delete a student account!", width=70, height=60)
        dlt_acc_title.place(x=60, y=-350)
        chng_acc_title = Label(changePassword_tab, text="Change password", width=70, height=60)
        chng_acc_title.place(x=60, y=-350)

        crt_emailLbl = Label(createAccount_tab, text="Email", font=("Comic Sans", 18))
        crt_emailLbl.place(x=55, y=150)

        crt_emailEntry = Entry(createAccount_tab, width="30")
        crt_emailEntry.place(x=200, y=155)

        crt_usernameLbl = Label(createAccount_tab, text="Username", font=("Comic Sans", 18))
        crt_usernameLbl.place(x=55, y=200)

        crt_usernameEntry = Entry(createAccount_tab, width="30")
        crt_usernameEntry.place(x=200, y=205)

        crt_passwordLbl = Label(createAccount_tab, text="Password", font=("Comic Sans", 18))
        crt_passwordLbl.place(x=55, y=250)

        crt_passwordEntry = Entry(createAccount_tab, width="30", show="*")
        crt_passwordEntry.place(x=200, y=255)

        crt_reTypePasswordLbl = Label(createAccount_tab, text="Re-type password", font=("Comic Sans", 18))
        crt_reTypePasswordLbl.place(x=55, y=300)

        crt_reTypePasswordEntry = Entry(createAccount_tab, width="30", show="*")
        crt_reTypePasswordEntry.place(x=260, y=305)

        crt_submitButton = Button(createAccount_tab, text="Create", width=5, font=("Comic sans", 10),
                                  command=lambda: connect_database(crt_emailEntry.get(),
                                                                   crt_usernameEntry.get(),
                                                                   crt_passwordEntry.get(),
                                                                   crt_reTypePasswordEntry.get()))
        crt_submitButton.place(x=200, y=350)


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

    submitButton = Button(adminWindow, text="Login", width=5, font=("Comic sans", 10), command=admin_submit)
    submitButton.grid()


if __name__ == '__main__':
    starter_page()
