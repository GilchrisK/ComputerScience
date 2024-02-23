#UNFINISHED - OPENFILE CODE IS NOT COMPLETE

from tkinter import *
from tkinter import filedialog

def openFile(): #FINISH CODE FOR OPENING A FILE AND PASTE IT HERE
    print("File has been opened!")




# def saveFile(): #SAVES A FILE
#     print("File has been saved!")
#     file = filedialog.asksaveasfile(initialdir="C:\\Users\\Gilch\\OneDrive\\Pycharm",#This will create it straight into your pycharm folder
#                                     defaultextension=".txt",
#                                     filetypes=[
#                                         ("Text file",".txt"),
#                                         ("HTML file", ".html"),
#                                         ("All files", ".*")
#                                     ])
#     filetext = str(text.get(1.0,END)) #stores writing from "text" into a variable
#     file.write(filetext)
#     file.close()

def cut(): #FINISH CODE FOR OPENING A FILE AND PASTE IT HERE
    print("You cut some text!")
def copy(): #FINISH CODE FOR OPENING A FILE AND PASTE IT HERE
    print("You copied some text!")
def paste(): #FINISH CODE FOR OPENING A FILE AND PASTE IT HERE
    print("You pasted some text!")

def make_window():
    from projectiles_code import projectile_window


def openQuiz():
    from projectileQuiz import projectileQuiz
    projectileQuiz()
    pass

window = Tk()
window.geometry("800x500")

#
# text = Text(window) #pack that allows you to write
# text.pack()
#
menubar = Menu(window) #creates a menu bar
window.config(menu=menubar)


fileMenu = Menu(menubar,tearoff=0,font=("Comic sans",20)) # tear off removes the extra unnecessary line # 'File' is the first menu
menubar.add_cascade(label="File",menu=fileMenu) # cascade allows the drop-down menu affect when you click on a menu

fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_separator() # this adds a line to separate the file commands
# fileMenu.add_command(label="Save",command=saveFile)
# fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit)
fileMenu.add_separator()


editMenu = Menu(menubar,tearoff=0,font=("Comic sanas",20))
menubar.add_cascade(label="Edit",menu=editMenu)

editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)

playButton = Button(window,text="Play",width=30, height=5, command=make_window)
playButton.pack(pady=100, padx=50)

quizButton = Button(window,text="Quiz",width=30, height=5, command=openQuiz)
quizButton.pack(pady=10, padx=150)





window.mainloop()
