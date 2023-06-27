from tkinter import *

def submit():
    input = text.get("1.0",END)
    print(input)

window = Tk()

text= Text(window,
           bg="light grey",
           font=("Arial", 35),
           height=8,
           width=20,
           pady=25,
           padx=25,
           fg="purple")
text.pack()

button = Button(window,
                text="submit",
                command=submit,
                )
button.pack()


window.mainloop()