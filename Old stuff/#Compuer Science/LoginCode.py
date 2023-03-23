import tkinter
from tkinter import *


def back(wx):
    wx.destroy()
    main()

def submit(win,user,password,Retype):
        main()


def main():
    # code for the main menu
    # from this window, I can go to log in or signin or exit

    win1 = Tk()
    win1.title("Welcome")
    win1.geometry("400x180")

    titleLabel = Label(win1, text=" Welcome to TKINTER programming")
    titleLabel.grid(row=0, column=0, columnspan=3, sticky="SNEW", pady=10, padx=10)

    exitButton = Button(win1, text="Exit", width=12, command=quit)
    exitButton.grid(row=1, column=0, padx=10, pady=30)

    loginButton = Button(win1, text="Login", width=12, command=lambda: login(win1))
    loginButton.grid(row=1, column=1, padx=10, pady=10)

    createButton = Button(win1, text="Create", width=12, command=lambda: create(win1))
    createButton.grid(row=1, column=2, padx=10, pady=10)

    mainloop()


def login(x):
    # code to create login screen
    x.destroy()
    win2 = Tk()
    win2.title("Login...")
    win2.geometry("400x180")

    titleLabel = Label(win2, text=" Please enter your login details... ")
    titleLabel.grid(row=0, column=0, columnspan=3, sticky="SNEW", pady=10, padx=10)

    loginLabelUsername = Label(win2, text="Username")
    loginLabelUsername.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    loginEntryUsername = Entry(win2, width="30")
    loginEntryUsername.grid(row=1, column=1, padx=10, pady=10, sticky="E")

    loginLabelPass = Label(win2, text="Password")
    loginLabelPass.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    loginEntryPass = Entry(win2, width="30")
    loginEntryPass.grid(row=2, column=1, padx=10, pady=10, sticky="E")




    backButton = Button(win2, text="Back", command=lambda: back(win2))
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)

    # print("login")


def create(w):
    w.destroy()
    win3 = Tk()
    win3.title("Create ... ")
    win3.geometry("400x260")



    titleLabel = Label(win3, text=" Please complete all fields to create your account...")
    titleLabel.grid(row=0, column=0, columnspan=3, sticky="SNEW", pady=10, padx=10)

    backButton = Button(win3, text="Back", command=lambda: back(win3))
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)

    loginLabelUsername = Label(win3, text="Username")
    loginLabelUsername.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    loginEntryUsername = Entry(win3, width="30")
    loginEntryUsername.grid(row=1, column=1, padx=10, pady=10, sticky="E")

    loginLabelPass = Label(win3, text="Password")
    loginLabelPass.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    loginEntryPass = Entry(win3, width="30")
    loginEntryPass.grid(row=2, column=1, padx=10, pady=10, sticky="E")

    loginLabelPassRetype = Label(win3, text="Retype your Password")
    loginLabelPassRetype.grid(row=3, column=0, padx=10, pady=10, sticky="W")

    loginEntryPassRetype = Entry(win3, width="30")
    loginEntryPassRetype.grid(row=3, column=1, padx=10, pady=10, sticky="E")

    submitButton = Button(win3, text="Submit", command=lambda: submit(win3))
    submitButton.grid(row=5, column=1, sticky="SNEW", padx=10, pady=10)

    mainloop()


def menu():
    # code for creating the application's menu

    pass


main()
