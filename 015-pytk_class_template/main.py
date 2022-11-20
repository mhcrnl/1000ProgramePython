#!/usr/bin/python3
# -*- coding: utf-8 -*-
# FILE      : main.py
# RUN       : python3 main.py
# CREATED BY: mhcrnl2@gmail.com
# DATE      : 20.11.2022
# SCOP      : Template for tkinter with class.
# --------------------------------------------------------------Begin file
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # Configure the root window.
        self.title("Aplicatia Mea")
        self.geometry("550x450")
        # Label
        self.label = ttk.Label(self, text="Salut, Tkinter!")
        self.label.pack()
        # Button
        self.button = ttk.Button(self, text="Apasa AICI!")
        self.button['command'] = self.button_clicked
        self.button.pack()

    def button_clicked(self):
        showinfo(title='Informativ', message='Aceasta este o info.')

if __name__ == "__main__":
    app = App()
    app.mainloop()
# ---------------------------------------------------------------End file

