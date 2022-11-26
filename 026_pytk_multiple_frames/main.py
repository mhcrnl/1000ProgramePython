#!/usr/bin/env python3
# https://zetcode.com/tkinter/introduction/

from tkinter import Tk, BOTH, Text, TOP, X, N, LEFT
from tkinter.ttk import Frame, Label, Entry

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Simple window")
        self.pack(fill=BOTH, expand=1)
        # -----------------------------------------------Frame1
        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Title", width=6)
        lbl1.pack(side=LEFT, padx=5, pady=5)

        entry1 = Entry(frame1)
        entry1.pack(fill=X, padx=5, expand=True)
        # ------------------------------------------------Frame2
        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Author", width=6)
        lbl2.pack(side=LEFT, padx=5, expand=True)

        entry2 = Entry(frame2)
        entry2.pack(fill=X, padx=5, expand=True)
        

def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example()
    root.mainloop()

if __name__ == "__main__":
    main()

    

