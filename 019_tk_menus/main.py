#!/usr/bin/python3
# -*- coding: utf-8 -*-
# FILE: 005_hello_world.py
# RUN : python3 005_hello_world.py
# --------------------------------------------------------------Begin file
from tkinter import *

def MyFunction():
    print("Hello, World!")

root = Tk()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=MyFunction)
filemenu.add_command(label="Open", command=MyFunction)
filemenu.add_command(label="Save", command=MyFunction)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)
#filemenu.add_command(label="File", command=MyFunction)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help index", command=MyFunction)
helpmenu.add_command(label="About", command=MyFunction)
helpmenu.add_command(label="Help...", command=MyFunction)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()
# ---------------------------------------------------------------End file

