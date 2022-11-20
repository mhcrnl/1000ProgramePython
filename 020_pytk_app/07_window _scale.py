#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        l = Label(self, bg="white", fg="black", width=20, text="empty")
        l.pack()

        s = Scale(self, label="try me", from_=0, to=10, orient=HORIZONTAL,
                  length=200, showvalue=0, tickinterval=2, resolution=0.01,
                  command=self.print_selection)
        s.pack()

    def print_selection(self,v):
        self.l.config(text="You have selected "+v)

# initialize tkinter
root = Tk()
app = Window(root)
#set window title
root.wm_title('Tkinter Window')
# show window
root.mainloop()
