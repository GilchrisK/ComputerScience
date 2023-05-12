import tkinter
from tkinter import *

def back(wx):
    wx.destroy()
    tkinter_project()

def submit(win, user, password, Retype):
    tkinter_project()

def tkinter_project():
    # code for the main menu
    # from this window, I can go to log in or signin or exit

    tkinter_labels = Tk()
    tkinter_labels.title("Welcome")
    tkinter_labels.geometry("400x180")

    titleLabel = Label(tkinter_labels, text=" Welcome to TKINTER programming")
    titleLabel.grid(row=0, column=0, columnspan=3, sticky="SNEW", pady=10, padx=10)

    exitButton = Button(tkinter_labels, text="Exit", width=10, command=quit)
    exitButton.grid(row=0, column=0, padx=10, pady=10)

    loginButton = Button(tkinter_labels, text="Login", width=10, command=lambda: login(tkinter_labels))
    loginButton.grid(row=1, column=2, padx=10, pady=10)




    mainloop()

def login(x):
    # code to create login screen
    x.destroy()
    tkinter_login = Tk()
    tkinter_login.title("Login...")
    tkinter_login.geometry("400x180")

    titleLabel = Label(tkinter_login, text=" Please enter your login details... ")
    titleLabel.grid(row=0, column=0, columnspan=3, sticky="SNEW", pady=10, padx=10)

    loginLabelUsername = Label(tkinter_login, text="Username")
    loginLabelUsername.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    loginEntryUsername = Entry(tkinter_login, width="30")
    loginEntryUsername.grid(row=1, column=1, padx=10, pady=10, sticky="E")

    loginLabelPass = Label(tkinter_login, text="Password")
    loginLabelPass.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    loginEntryPass = Entry(tkinter_login, width="30")
    loginEntryPass.grid(row=2, column=1, padx=10, pady=10, sticky="E")




    backButton = Button(tkinter_login, text="Back", command=lambda: back(tkinter_login))
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)

    # print("login")


tkinter_project()