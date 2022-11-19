#!/usr/bin/python3
# -*- coding: utf-8 -*-
# FILE      : main.py
# RUN       : python3 main.py
# CREATED BY: mhcrnl2@gmail.com
# DATE      : 19.11.2022
# --------------------------------------------------------------Begin file
from tkinter import *

root = Tk()

Label(root, text="Username").grid(row=0, sticky=W)
Label(root, text="Password").grid(row=1, sticky=W)

Entry(root).grid(row=0, column=1, sticky=E)
Entry(root).grid(row=1, column=1, sticky=E)

Button(root, text="Login").grid(row=2, column=1, sticky=E)

root.mainloop()

print("Hello, World!")
# ---------------------------------------------------------------End file

