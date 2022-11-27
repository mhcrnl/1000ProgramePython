#!/usr/bin/env python3
# https://zetcode.com/tkinter/introduction/

from tkinter import Tk, BOTH, Text, TOP, X, N, LEFT
from tkinter.ttk import Frame, Label, Entry, Button

import sqlite3
from sqlite3 import Error

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
        lbl2.pack(side=LEFT, padx=5, pady=5)

        entry2 = Entry(frame2)
        entry2.pack(fill=X, padx=5, expand=True)
        # ---------------------------------------------------Frame3
        frame3 = Frame(self)
        frame3.pack(fill=BOTH, expand=1)

        lbl3 = Label(frame3, text="Review", width=6)
        lbl3.pack(side=LEFT, anchor=N, padx=5,pady=5)

        txt = Text(frame3)
        txt.pack(fill=BOTH, pady=5, padx=5, expand=True)
        # ---------------------------------------------------Frame4
        frame4 = Frame(self)    
        frame4.pack(fill=BOTH, expand=1)

        save_btn = Button(frame4, text="Save", command=self.save_to_sqlite3)
        save_btn.pack(side=LEFT, anchor=N)

    def save_to_sqlite3(self):
        try:
            con = sqlite3.connect('biblioteca.db')
            print("Saving to sqlite3")
        except Error as e:
            print(e)
            con = None
        finally:
            con.close()

def main():
    root = Tk()
    root.geometry("650x550+400+300")
    app = Example()
    root.mainloop()

if __name__ == "__main__":
    main()

    

