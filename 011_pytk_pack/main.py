#!/usr/bin/python3
# -*- coding: utf-8 -*-
# FILE      : main.py
# RUN       : python3 main.py
# CREATED BY: mhcrnl2@gmail.com
# DATE      : 19.11.2022
# --------------------------------------------------------------Begin file
from tkinter import *

root = Tk()

#mylabel = Label(root, text = "Sunt o eticheta!")
#mybutton = Button(root, text="Sunt un buton!")

Button(root, text="A").pack(side=LEFT,expand=YES, fill=Y)
#mylabel.pack()
#mybutton.pack()

Button(root, text="B").pack(side=TOP, expand=YES, fill=BOTH)

Button(root, text="C").pack(side=RIGHT, expand=YES, fill=NONE, anchor=NE)

Button(root, text="D").pack(side=LEFT, expand=NO, fill=Y)

Button(root, text="E").pack(side=TOP, expand=NO, fill=BOTH)

Button(root, text="F").pack(side=RIGHT, expand=NO, fill=NONE)

Button(root, text="G").pack(side=BOTTOM, expand=YES, fill=Y)

Button(root, text="H").pack(side=TOP, expand=YES, fill=BOTH)

Button(root, text="I").pack(side=RIGHT, expand=NO)

Button(root, text="J").pack(anchor=SE)

#mylabel.pack()
#mybutton.pack()
root.mainloop()

print("Hello, World!")


# ---------------------------------------------------------------End file

