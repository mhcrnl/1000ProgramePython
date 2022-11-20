#!/usr/bin/python3

from tkinter import *
# pip install pillow
from PIL import Image, ImageTk

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.pack(fill=BOTH, expand=1)

        load = Image.open("index.jpeg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

# initialize tkinter
root = Tk()
app = Window(root)
#set window title
root.wm_title('Tkinter Window')
root.geometry("200x120")
# show window
root.mainloop()
