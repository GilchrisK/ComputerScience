from tkinter import *
def help_page():
    help_window = Tk()
    help_window.title("Help")
    help_window.geometry("480x180")
    help_window.maxsize(480,180)
    help_window.minsize(480,180)

    help_window.config(bg="dark grey")

    info_lbl1 = Label(help_window, text="This is the following information that may help you with the simulation:", font=("Arial", 11))
    info_lbl1.grid(row=0)

    info_lbl2 = Label(help_window, text="1. Pressing '1' or the line image will show the path of the projectile", font=("Arial", 11))
    info_lbl2.grid(row=2)

    info_lbl3 = Label(help_window, text="2. Click the ruler image to show the distances on the ground", font=("Arial", 11))
    info_lbl3.grid(row=4)

    info_lbl4 = Label(help_window, text="3. Click the graph image or the enter button mid launch to see graph", font=("Arial", 11))
    info_lbl4.grid(row=6)

    info_lbl5 = Label(help_window, text="4. Use up/down arrows to control the angle of the projectile", font=("Arial", 11))
    info_lbl5.grid(row=8)

    info_lbl6 = Label(help_window, text="5. Use left/right arrows to control the speed of the projectile", font=("Arial", 11))
    info_lbl6.grid(row=10)
def make_window():
    window.destroy()
    from projectiles_code import projectile_window



def openQuiz():
    window.destroy()
    from projectileQuiz import show_question
    show_question()

def run_homePage():
    global window
    window = Tk()
    window.title("Projectiles Homepage")
    window.geometry("800x500")
    window.maxsize(800,500)
    window.minsize(800,500)
    window.config(bg="light blue")

    menubar = Menu(window) #creates a menu bar
    window.config(menu=menubar)


    fileMenu = Menu(menubar,tearoff=0,font=("Comic sans",20)) # tear off removes the extra unnecessary line
                                                                # 'File' is the first menu
    menubar.add_cascade(label="File",menu=fileMenu) # cascade allows the drop-down menu affect when you click on a menu

    fileMenu.add_command(label="Exit",command=quit)
    fileMenu.add_separator()


    playButton = Button(window,bg="#fff5e6",text="Play",width=30, height=5, command=make_window)
    playButton.pack(pady=100, padx=50)

    helpButton = Button(window,bg="light pink", text="?", width=5, height=2, command=help_page)
    helpButton.place(x=550,y=120)

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