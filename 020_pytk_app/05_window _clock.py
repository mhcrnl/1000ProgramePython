#!/usr/bin/python3

import time
from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.label = Label(text="", fg="Red", font=("Helvetica", 18))
        self.label.place(x=50, y=80)
        self.clock()

    def clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.after(1000, self.clock)

# initialize tkinter
root = Tk()
app = Window(root)
#set window title
root.wm_title('Tkinter Window')
root.geometry("200x200")
root.after(1000, app.clock)
# show window
root.mainloop()
