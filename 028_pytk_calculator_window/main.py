#!/usr/bin/env python3
# https://zetcode.com/tkinter/introduction/

from tkinter import Tk, BOTH, W, E
from tkinter.ttk import Frame, Button, Entry, Style

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Calculator window")
        Style().configure("Button", padding=(0,5,0,5),font='serif 10')

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)

        entry = Entry(self)
        entry.grid(row=0, columnspan=4, sticky=W+E)

        self.pack(fill=BOTH, expand=1)

def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example()
    root.mainloop()

if __name__ == "__main__":
    main()

    

