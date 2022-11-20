#!/usr/bin/python3
# -*- coding: utf-8 -*-
# FILE: 010_tkpy_window.py
# RUN : python3 010_tkpy_window.py
# CREATED BY: mhcrnl2@gmail.com
# DATE:19.11.2022
# --------------------------------------------------------------Begin file
from tkinter import *

root = Tk()

mylabel = Label(root, text = "Sunt o eticheta!")
mybutton = Button(root, text="Sunt un buton!")

mylabel.pack()
mybutton.pack()

root.mainloop()

print("Hello, World!")


# ---------------------------------------------------------------End file

