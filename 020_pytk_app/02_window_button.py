#!/usr/bin/python3
# TUTORIAL: https://pythonbasics.org/tkinter-button/

from tkinter import *

class Window(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        # widget can take all window
        self.pack(fill=BOTH, expand=1)
        # create button, link it to exit
        b_exit = Button(self, text="Exit", command=self.f_exit)
        # place button at (0,0)
        b_exit.place(x=0, y=0)

    def f_exit(self):
        exit()

# initialize tkinter
root = Tk()
app = Window(root)
#set window title
root.wm_title('Tkinter Window')
root.geometry("320x200")
# show window
root.mainloop()
