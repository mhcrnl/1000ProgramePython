#!/usr/bin/env python3
# https://zetcode.com/tkinter/introduction/

from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Style
from PIL import Image, ImageTk

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Absolute positioning")
        self.pack(fill=BOTH, expand=1)

        Style().configure("TFrame", background="#333")

        board = Image.open("img_01.JPG")
        img_01 = ImageTk.PhotoImage(board)
        label1 = Label(self, image=img_01)
        label1.image = img_01
        label1.place(x=20, y=20)

        board2 = Image.open("img_02.JPG")
        img_02 = ImageTk.PhotoImage(board2)
        label2 = Label(self, image=img_02)
        label2.image = img_02
        label2.place(x=40, y=160)

        board3 = Image.open("img_03.JPG")
        img_03 = ImageTk.PhotoImage(board3)
        label3 = Label(self, image=img_03)
        label3.image = img_03
        label3.place(x=170, y=50)

def main():
    root = Tk()
    root.geometry("350x250+300+300")
    app = Example()
    root.mainloop()

if __name__ == "__main__":
    main()

    

