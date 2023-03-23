# --------------------------   BMI Calculator  -----------------------------------
# import tkinter
from tkinter import *
from tkinter import messagebox


def clearBoxes(e1, e2):
    # e1 and e2 are the entry boxes  to be cleared
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e1.focus()
    return



def isvalid(f,h, w):
    if h >= 0.5 and w>= 20:
        return True
    else:
        messagebox.showinfo(Tile = "Data Entry Error:", message="Enter reasonable height (m) and weight(Kg) ")
        msgBox = messagebox.askquestion(title="continue...", message="Do you want to continue?")
        msgBox = messagebox.askquestion(title="Error ", message="Do you want to try again?")
        if msgBox == "yes":
            f.destroy()
            createGUI()
        else:
            messagebox.showinfo(Tile = "Thank You:", message="Thank you or using my BMI calculator ") ,
            quit()

def calcBMI(f, w, h):
    # f is the window (form) used in CreateGUI() function
    h = float(h.get())
    w = float(w.get())
    if isvalid(f,h, w):

    # call a IsValid to validate h and w,
    # if IsValid(w, h) returns True, Carry out the BMI calculation


        bmi = w / (h * h)
        bmi = round(bmi, 2)  # calculate bmi
        result = "your BMI is   " + str(bmi)
        messagebox.showinfo(title="BMI value", message=result)
        msgBox = messagebox.askquestion(title="continue...", message="Do you want to continue?")
        if msgBox == "yes":
            f.destroy()
            createGUI()
        else:
            # add code to confirm that the user wants to exit before exit,
            quit()
        return




def createGUI():
    form = Tk()
    form.title("Welcome to BMI calculator")
    form.geometry("500x220")
    # creating welcome label:
    welcomeLabel = Label(form, text=" Welcome to my BMI calculator")
    welcomeLabel.config(font=("Courier", 14))
    welcomeLabel.grid(row=0, column=0, columnspan=3, sticky="W", padx=10, pady=10)
    # creating weight and height labels:
    weightLabel = Label(form, text="Weight in Kg")
    weightLabel.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    heightLabel = Label(form, text="Height in Meters")
    heightLabel.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    helpLabel = Label(form, text=" enter height(m)and weight(Kg)")
    helpLabel.grid(row=1, rowspan=2, column=2, padx=10, pady=10)
    # creating text-boxes (entry boxes):
    weightEntry = Entry(form, width="30")
    weightEntry.grid(row=1, column=1, padx=10, pady=10, sticky="E")
    heightEntry = Entry(form, width="30")
    heightEntry.grid(row=2, column=1, padx=10, pady=10, sticky="E")
    # creating the buttons:
    exitButton = Button(form, text="Exit", width=12, command=quit)
    exitButton.grid(row=3, column=0, padx=10, pady=10)

    clearButton = Button(form, text="Clear", width=12, command=lambda: clearBoxes(weightEntry, heightEntry))
    clearButton.grid(row=3, column=1, padx=10, pady=10)

    calcButton = Button(form, text="Calculate", width=12, command=lambda: calcBMI(form, weightEntry,
                                                                                  heightEntry))
    # later we add command to call a function
    calcButton.grid(row=3, column=2, padx=10, pady=10)

    weightEntry.focus()  # set the focus to eightEntry box (the top one)
    # makes it easy to user to avoid clicking the box before
    # we enter the data
    mainloop()
    return


createGUI()
