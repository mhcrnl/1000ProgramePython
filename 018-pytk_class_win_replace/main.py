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

class InputFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # Setup the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        self.__create_widgets()

    def __create_widgets(self):
        # Find what
        ttk.Label(self, text='Find what:').grid(column=0, row=0, sticky=tk.W)
        keyword = ttk.Entry(self, width=30)
        keyword.focus()
        keyword.grid(column=1, row=0, sticky=tk.W)
        # Replace with.
        ttk.Label(self, text='Replace with:').grid(column=0, row=1, sticky=tk.W)
        replacement = ttk.Entry(self, width=30)
        replacement.grid(column=1, row=1, sticky=tk.W)
        # Match case checkbox
        match_case = tk.StringVar()
        match_case_check = ttk.Checkbutton( self, text='Match case',
                                            variable=match_case,
                                            command=lambda: print(match_case.get()))
        match_case_check.grid(column=0, row=2, sticky=tk.W)
        # Wrap Around checkbox
        wrap_around = tk.StringVar()
        wrap_around_check = ttk.Checkbutton(self, variable=wrap_around,
                                            text='Wrap around',
                                            command=lambda: print(wrap_around.get()))
        wrap_around_check.grid(column=0, row=3, sticky=tk.W)

        for widget in self.winfo_children():
            widget.grid(padx=0, pady=5)

class ButtonFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # Setup the grid layout manager
        self.columnconfigure(0, weight=1)

        self.__create_widgets()

    def __create_widgets(self):
        ttk.Button(self, text='Find Next').grid(column=0, row=0)
        ttk.Button(self, text='Replace').grid(column=0, row=1)
        ttk.Button(self, text='Replace All').grid(column=0, row=2)
        ttk.Button(self, text='Cancel').grid(column=0, row=3)

        for widget in self.winfo_children():
            widget.grid(padx=0, pady=3)
        

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configure the root window.
        self.title("Aplicatia Mea")
        self.geometry("550x450")
        self.resizable(0,0)
        # Window only(remove the minimize/maximize button)
        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=1)

        self.__create_widgets()

    def __create_widgets(self):
        # Create the input frame
        input_frame = InputFrame(self)
        input_frame.grid(column=0, row=0)
        # Create the button frame.
        button_frame = ButtonFrame(self)
        button_frame.grid(column=1, row=0)
        '''
        # Label
        self.label = ttk.Label(self, text="Salut, Tkinter!")
        self.label.pack()

        # Button
        self.button = ttk.Button(self, text="Apasa AICI!")
        self.button['command'] = self.button_clicked
        self.button.pack()

    def button_clicked(self):
        showinfo(title="Information", message="Salut, Tkinter!")
        '''
if __name__ == "__main__":
    app = App()
    app.mainloop()
# ---------------------------------------------------------------End file

