from tkinter import *

def CreateGUI():
    form = Tk() #generate value
    form.title("Welcome to BMI calculator")
    form.geometry("1000x440")
    welcomeLabel = Label(form, text=" Welcome to my BMI calculator")
    welcomeLabel.config(font=("Courier", 10))
    welcomeLabel.grid(row=0, column=0, columnspan=3, sticky="W", padx=10, pady=10)
    weightLabel = Label(form, text="Weight in Kg")###
    weightLabel.grid(row=1, column=0, padx=10, pady=10, sticky="W")###
    heightLabel = Label(form, text="Height in Meters")
    heightLabel.grid(row=2, column=0, padx=10, pady=10, sticky="W")
    helpLabel = Label(form, text=" enter height(m)and weight(Kg)")
    helpLabel.grid(row=1, rowspan=2, column=2, padx=10, pady=10)
    weightEntry = Entry(form, width="30")###
    weightEntry.grid(row=1, column=1, padx=10, pady=10, sticky="E")###

    form.mainloop()
CreateGUI()


