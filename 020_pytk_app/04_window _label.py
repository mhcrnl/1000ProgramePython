#!/usr/bin/python3

from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        text = Label(self, text="Just do it!")
        text.place(x=70, y=90)
        # text.pack()

# initialize tkinter
root = Tk()
app = Window(root)
#set window title
root.wm_title('Tkinter Window')
root.geometry("200x200")
# show window
root.mainloop()
