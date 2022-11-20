#!/usr/bin/python3
# -*- coding: utf-8 -*-
# FILE      : main.py
# RUN       : python3 main.py
# CREATED BY: mhcrnl2@gmail.com
# DATE      : 20.11.2022
# SCOP      : Template for tkinter with frame class.
# --------------------------------------------------------------Begin file
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        options = {'padx':5, 'pady':5}
        # Label
        self.label = ttk.Label(self, text="Salut, Tkinter!")
        self.label.pack(**options)
        # Button
        self.button = ttk.Button(self, text="Apasa AICI!")
        self.button['command'] = self.button_clicked
        self.button.pack(**options)
        # Show the frame on the container.
        self.pack(**options)

    def button_clicked(self):
        showinfo(title='Informativ', message='Aceasta este o info.')

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # Configure the root window.
        self.title("Aplicatia Mea")
        self.geometry("550x450")

if __name__ == "__main__":
    app = App()
    frame = MainFrame(app)
    app.mainloop()
# ---------------------------------------------------------------End file

