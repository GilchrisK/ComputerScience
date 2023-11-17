#
#NOT FINISHEDDDDDDDDDDDDDDDDDDDD
#
from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\Gilch\\OneDrive\\Pycharm",#This will create it straight into your pycharm folder
                                    defaultextension=".txt",
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*")
                                    ])
    filetext = str(text.get(1.0,END)) #stores writing from "text" into a variable
    file.write(filetext)
    file.close()

window = Tk()

button = Button(window,text="save",command=saveFile)
button.pack()

text = Text(window)
text.pack()





window.mainloop()