import sqlite3
from tkinter import *
from tkinter import ttk  # module that contains different widgets such as the notebook widget
# import project_saveData





def back(xy):
    xy.destroy()
    starter_page()

def goToHomePage():
    adminMainPage.destroy()
    starter_page()

def runProjectileGame():
    from projectiles_code import main

def runProjectileQuiz():
    starter_Window.destroy()
    from projectileQuiz import check_answer

#########################################################
# SQL SECTION
class LoginSystem():
    def createTable(self):
        try:
            conn = sqlite3.connect('accounts.db')

            conn.execute('''CREATE TABLE IF NOT EXISTS USERS 
                           (Email      TEXT NOT NULL,
                           UserName      TEXT     PRIMARY KEY     NOT NULL,
                            Password      TEXT    NOT NULL);''')
            conn.close()
            return True
        except:
            return False


    def insertData(self, givenUser, givenPassword, givenEmail):

        try:
            conn = sqlite3.connect('accounts.db')
            # insert data into database table
            conn.execute('''insert into USERS  (UserName, Password, Email) values (?, ?,?)''',
                         (givenUser, givenPassword,givenEmail))
            conn.commit()  # do not forget to commit the data (i.e. save the data on the table
            conn.close()
            return True
        except:
            return False


    def checkifExist(self,givenUser, givenPassword):
        try:
            conn = sqlite3.connect("accounts.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM USERS WHERE UserName = ? AND Password = ?",
                           (givenUser, givenPassword))
            if cursor.fetchone():
                conn.close()
                return True
            else:
                conn.close()
                return False
        except sqlite3.Error as e:
            print("Error:",e)
            return False

    def databaseLogin(self, User_entry, password_entry):
        User = User_entry.get()
        Password = password_entry.get()
        if self.checkifExist(givenUser=User, givenPassword=Password):
            studentWindow.destroy()
            from Projectiles_HomePage import run_homePage
            run_homePage()
        else:
            messagebox.showerror("Error","Problem within the field inputs")

    def changePassword(self, givenUser, newPassword):
        try:
            conn = sqlite3.connect("accounts.db")
            cursor = conn.cursor()
            cursor.execute("UPDATE USERS SET Password = ? WHERE UserName = ?", (newPassword, givenUser))
            conn.commit()
            conn.close()
            messagebox.showinfo("Successful", "Password was successfully changed")
            return True
        except sqlite3.Error as e:
            print("Error:", e)
            return False

    def deleteAllUsers(self):
        try:
            conn = sqlite3.connect("accounts.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM USERS")
            conn.commit()
            conn.close()
            messagebox.showinfo("Successful","All users were successfully deleted from the database")
            return True
        except sqlite3.Error as e:
            print("Error:", e)
            return False


#########
def on_login_button_click(studentEntry_Username,studentEntry_Password):
    login_system.databaseLogin(studentEntry_Username, studentEntry_Password)

def on_change_password_click(username, new_password):
    login_system.changePassword(username, new_password)

def on_delete_all_users_click():
    login_system.deleteAllUsers()
def checkLogin(username, password):
    try:
        conn = sqlite3.connect("accounts.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM USERS WHERE UserName = ? AND Password = ?", (username, password))
        if cursor.fetchone():
            conn.close()
            return True
        else:
            conn.close()
            return False
    except sqlite3.Error as e:
        print("Error:", e)
        return False
login_system = LoginSystem()

#######################################################
def starter_page():
    global starter_Window
    starter_Window = Tk()
    starter_Window.geometry("950x800")
    starter_Window.minsize(950, 800)
    starter_Window.maxsize(950, 800)
    starter_Window.config(bg="#bad7e7", padx=100, pady=150, relief=SUNKEN)
    starter_Window.title("Main Page")
    global notebook
    notebook = ttk.Notebook(starter_Window)  # A widget that manages a collection of windows/displays

    global guest_tab
    login_tab = Frame(notebook, padx=100)  # This will be a new frame for tab1
    guest_tab = Frame(notebook, padx=100)  # New frame for tab2

    notebook.add(login_tab, text="Log in")
    notebook.add(guest_tab, text="Guest")
    notebook.pack()  # This will expand to fill any space


    login_lbl1 = Label(login_tab, text="Projectile Simulator!", font=("Comic Sans", 20), width=20, height=2, anchor='center',
                       bg="light grey")
    login_lbl1.pack(pady=60)
    login_lbl2 = Label(login_tab, text="Choose the account to login with", font=("Comic sans", 20), bg="light grey")
    login_lbl2.place(x=80, y=160)

    guest_lbl1 = Label(guest_tab, text="Guest account!", width=70, height=60,font=("Arial",35))
    guest_lbl1.pack()

    play_btn = Button(guest_tab, text= "Play", width=20, height=5, command=lambda: runProjectileGame(),
                     bg="light grey")
    play_btn.place(x=100, y=290)

    quiz_btn = Button(guest_tab, text="Quiz", width=20, height=5, command=lambda: runProjectileQuiz(),
                      bg="light grey")
    quiz_btn.place(x=300, y=290)

    admin_btn = Button(login_tab, text="Admin", width=20, height=5, command=lambda: adminPage(login_tab),
                       bg="light grey")
    admin_btn.place(x=100, y=300)

    student_btn = Button(login_tab, text="Student", width=20, height=5, command=lambda: studentPage(login_tab),
                         bg="light grey")
    student_btn.place(x=320, y=300)

    guest_btn = Button(login_tab, text="Guest", width=10, height=1, command=switch_signUp)
    guest_btn.place(x=330, y=420)

    login_lbl3 = Label(login_tab, text="Click here to use a guest account...", font=("Comic Sans", 11))
    login_lbl3.place(x=78, y=423)
    ###########################

    mainloop()


######################################

from tkinter import messagebox


def admin_submit():
    global a
    global b
    global c

    def clear():
        a.delete(0, END)
        b.delete(0, END)
        c.delete(0, END)

    def connect_database(a, b, c, d):
        if a == '' or b == '' or c == '' or d == '':
            messagebox.showerror("Error", "All fields must be completed")
        elif c != d:
            messagebox.showerror("Error", "Passwords do not match")
        else:
            # Assuming project_validation.validate_studentEmail, project_validation.isValidUsername,
            # and project_validation.isValidPassword are defined elsewhere and return True or False
            import project_validation
            flagA = project_validation.validate_studentEmail(a)
            flagB = project_validation.isValidUsername(b)
            flagC = project_validation.isValidPassword(c)

            if flagA and flagB and flagC:
                try:
                    con = sqlite3.connect('accounts.db')  # Assuming 'example.db' is the SQLite database file
                    mycursor = con.cursor()
                except sqlite3.Error as e:
                    messagebox.showerror("Error", f"Database Connectivity Issue: {e}")
                    return

                try:
                    mycursor.execute("CREATE TABLE IF NOT EXISTS USERS (Email TEXT, UserName TEXT, Password TEXT)")
                    query = "INSERT INTO USERS(Email, UserName, Password) VALUES (?, ?, ?)"
                    mycursor.execute(query, (a, b, c))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Registration is successful")
                except sqlite3.Error as e:
                    messagebox.showerror("Error", f"Database Error: {e}")
                finally:
                    if con:
                        con.close()
            else:
                messagebox.showerror("Error", "Invalid information")


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
        adminMainPage.maxsize(800, 650)
        adminMainPage.config(bg="light blue")
        adminMainPage.title("Admin Main Page")
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

        crt_acc_title = Label(createAccount_tab, text="Create a student account!"
                                                      " Enter the inputs through the fields", width=70, height=60, font=("Arial"))
        crt_acc_title.place(x=30, y=-450)

        dlt_acc_title = Label(deleteAccount_tab, text="Delete all user accounts! Once clicked, all user data will be permanently lost", width=70, height=60, font=("Arial"))
        dlt_acc_title.place(x=0, y=-450)

        chng_acc_title2 = Label(changePassword_tab, text="Enter the username of the student and then the new password",
                               width=70, height=60, font=("Arial"))
        chng_acc_title2.place(x=10, y=-370)

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

        homeButton = Button(createAccount_tab, text="HomePage", width=10, font=("Comic sans", 10),
                            command= lambda: goToHomePage())
        homeButton.place(x=100, y=350)

        crt_submitButton = Button(createAccount_tab, text="Create", width=5, font=("Comic sans", 10),
                                  command=lambda: connect_database(crt_emailEntry.get(),
                                                                   crt_usernameEntry.get(),
                                                                   crt_passwordEntry.get(),
                                                                   crt_reTypePasswordEntry.get()))
        crt_submitButton.place(x=200, y=350)


        changePass_usernameLbl = Label(changePassword_tab, text="Username", font=("Comic Sans", 18))
        changePass_usernameLbl.place(x=55, y=200)

        changePass_usernameEntry = Entry(changePassword_tab, width="30")
        changePass_usernameEntry.place(x=200, y=205)

        changePass_passwordLbl = Label(changePassword_tab, text="New Password", font=("Comic Sans", 18))
        changePass_passwordLbl.place(x=55, y=250)

        changePassPasswordEntry = Entry(changePassword_tab, width="30", show="*")
        changePassPasswordEntry.place(x=230, y=255)

        changePasswordButton = Button(changePassword_tab, text="Change Password",
                                      command=lambda: on_change_password_click(changePass_usernameEntry.get(),
                                                                               changePassPasswordEntry.get()))
        changePasswordButton.place(x=250,y=300)

        deleteAllUsersButton = Button(deleteAccount_tab, text="Delete All Users", command=on_delete_all_users_click, width=30, height=10,bg="red")
        deleteAllUsersButton.place(x=200, y=250)
################################
def switch_signUp():
    notebook.select(tab_id=guest_tab)


#################################

def studentPage(y):
    global studentWindow
    starter_Window.destroy()
    studentWindow = Tk()
    studentWindow.config(bg="Light blue")
    studentWindow.title("Student Login")
    studentWindow.geometry("500x400")
    studentWindow.minsize(500, 400)
    studentWindow.maxsize(500, 400)


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

    loginButton = Button(studentWindow, text= "login", command =lambda: on_login_button_click(studentEntry_Username,studentEntry_Password))
    loginButton.grid(row=4, column=1, sticky="SNEW", padx=10, pady=10)



#####################################
def adminPage(x):
    global adminEntry_Username
    global adminEntry_Password
    global adminWindow
    global admin_submit
    starter_Window.destroy()
    adminWindow = Tk()
    adminWindow.geometry("500x400")
    adminWindow.title("Admin Login")
    adminWindow.config(bg="Light blue")
    adminWindow.minsize(500,400)
    adminWindow.maxsize(500, 400)

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