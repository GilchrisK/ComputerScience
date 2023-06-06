import tkinter
from tkinter import *


def back(wx):
    wx.destroy()
    tkinter_project()


def tkinter_project():
    # code for the main menu
    # from this window, I can go to log in or signin or exit

    win1 = Tk() #win = window
    win1.title("Welcome")
    win1.geometry("400x180")

    titleLabel = Label(win1, text=" Welcome to TKINTER programming")
    titleLabel.grid(row=0, column=0, columnspan=3, sticky="SNEW", pady=10, padx=10)

    exitButton = Button(win1, text="Exit", width=12, command=quit)
    exitButton.grid(row=1, column=0, padx=10, pady=30)

    loginButton = Button(win1, text="Login", width=12, command=lambda: login(win1))
    loginButton.grid(row=1, column=1, padx=10, pady=10)

    signinButton = Button(win1, text="Sign in", width=12, command=lambda: signin(win1))
    signinButton.grid(row=1, column=2, padx=10, pady=10)



    # btn_admin = Button(win2,text="Admin", width=12,)

    mainloop()


def login(w):
    # code to create login screen
    w.destroy()
    win2 = Tk()
    win2.title("Choose your user")
    win2.geometry("400x200")

    btn_admin = Button(win2,text="Admin", width=12, command=lambda: login(win2))
    btn_admin.grid(row=1,column=1,padx=10,pady=10)

    mainloop()

def signin(w):
    w.destroy()
    win3 = Tk()
    win3.title("Sign in ... ")
    win3.geometry("400x180")

    titleLabel = Label(win3, text=" Please complete all fields ")
    titleLabel.grid(row=0, column=0, columnspan=3, sticky="SNEW", pady=10, padx=10)

    backButton = Button(win3, text="Back", command=lambda: back(win3))
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)

    mainloop()


def menu():
    # code for creating the application's menu

    pass


tkinter_project()

