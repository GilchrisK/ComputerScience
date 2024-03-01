#UNFINISHED - OPENFILE CODE IS NOT COMPLETE
from tkinter import *
from tkinter import filedialog

def make_window():
    from projectiles_code import projectile_window

def openQuiz():
    window.destroy()
    from projectileQuiz import show_question

def run_homePage():
    global window
    window = Tk()
    window.title("Projectiles Homepage")
    window.geometry("800x500")
    window.config(bg="#666699")

    menubar = Menu(window) #creates a menu bar
    window.config(menu=menubar)


    fileMenu = Menu(menubar,tearoff=0,font=("Comic sans",20)) # tear off removes the extra unnecessary line
                                                                # 'File' is the first menu
    menubar.add_cascade(label="File",menu=fileMenu) # cascade allows the drop-down menu affect when you click on a menu

    fileMenu.add_command(label="Exit",command=quit)
    fileMenu.add_separator()


    playButton = Button(window,bg="#fff5e6",text="Play",width=30, height=5, command=make_window)
    playButton.pack(pady=100, padx=50)

    quizButton = Button(window,bg="#fff5e6",
                        text="Quiz",
                        width=30,
                        height=5,
                        command=openQuiz
                        )
    quizButton.pack(pady=10,
                    padx=150
                    )

    window.mainloop()

if __name__ == '__main__':
    run_homePage()
