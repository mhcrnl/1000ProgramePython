#!/usr/bin/env python3
# https://zetcode.com/tkinter/introduction/

from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Button, Style

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Centered window")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

        self.quit_button()

    def centerWindow(self):
        w=290
        h=150

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw-w)/2
        y = (sh -h)/2
        self.master.geometry('%dx%d+%d+%d' %(w,h,x,y))

    def quit_button(self):
        quitButton = Button(self, text="Quit", command=self.close)
        quitButton.place(x=50, y=50)

    def close(self):
        self.master.destroy()

def main():
    root = Tk()
    # root.geometry("250x150+300+300")
    app = Example()
    root.mainloop()

if __name__ == "__main__":
    main()

    

