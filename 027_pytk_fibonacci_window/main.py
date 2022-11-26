#!/usr/bin/env python3
# https://zetcode.com/tkinter/introduction/

from tkinter import Tk, BOTH, Entry, Button
from tkinter.ttk import Frame
import fibonacci


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Simple window")
        self.pack(fill=BOTH, expand=1)

        self.fib_ent = Entry(self)
        self.fib_ent.pack()

        self.fib_ext = Entry(self)
        self.fib_ext.pack()

        cal_btn = Button(self, text="Calculeaza", command=self.f_calc)
        cal_btn.pack()

    def f_calc(self):
        print(self.fib_ent.get())
        fib = int(self.fib_ent.get())
        fib2 = str(fibonacci.Fibonacci(fib))
        self.fib_ext.insert(0,fib2)

def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example()
    root.mainloop()

if __name__ == "__main__":
    main()

    

