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
        Style().configure("TButton", padding=(0,5,0,5),font='serif 10')

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

        cls = Button(self, text="Cls")
        cls.grid(row=1, column=0)

        bck = Button(self, text="Back")
        bck.grid(row=1, column=1)

        lbl = Button(self)
        lbl.grid(row=1, column=2)
        
        clo = Button(self, text="Close", command=self.master.quit)
        clo.grid(row=1, column=3)

        seven = Button(self, text="7")
        seven.grid(row=2, column=0)

        eight = Button(self, text="8")
        eight.grid(row=2, column=1)

        nine = Button(self, text="9")
        nine.grid(row=2, column=2)

        div =  Button(self, text="/")
        div.grid(row=2, column=3)

        self.pack()

def main():
    root = Tk()
    root.geometry("350x250+500+400")
    app = Example()
    root.mainloop()

if __name__ == "__main__":
    main()

    

