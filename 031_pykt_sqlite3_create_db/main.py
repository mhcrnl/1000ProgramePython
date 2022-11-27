#!/usr/bin/env python

import tkinter as tk
from tkinter import ttk

import sqlite3
from sqlite3 import Error

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Sqlite3 test')
        self.geometry('500x500')
        self.resizable(width=False, height=False)

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        
        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self, text='Database name :')
        self.label.grid(row=0, column=0, columnspan=1)

        self.entry = ttk.Entry(self)
        self.entry.grid(row=0, column=1, columnspan=1)

        self.button = ttk.Button(self, text='Create', command=self.create_database)
        self.button.grid(row=0, column=2, columnspan=1)

        self.lb_nume = ttk.Label(self, text='Table name : ')
        self.lb_nume.grid(row=1, column=0, columnspan=1)

        self.ent_nume = ttk.Entry(self)
        self.ent_nume.grid(row=1, column=1, rowspan=1)

        self.lb_id = ttk.Label(self, text='ID : ')
        self.lb_id.grid(row=2, column=0, columnspan=1)
        
        self.ent_id = ttk.Entry(self)
        self.ent_id.grid(row=2, column=1, rowspan=1)

        self.lb_name = ttk.Label(self, text='Name : ')
        self.lb_name.grid(row=3, column=0, columnspan=1)

        self.ent_name = ttk.Entry(self)
        self.ent_name.grid(row=3, column=1, rowspan=1)

        self.lb_salary = ttk.Label(self, text='Salary : ')
        self.lb_salary.grid(row=4, column=0, columnspan=1)

        self.ent_salary = ttk.Entry(self)
        self.ent_salary.grid(row=4, column=1, rowspan=1)

        self.lb_department = ttk.Label(self, text='Department : ')
        self.lb_department.grid(row=5, column=0, columnspan=1)

        self.ent_department = ttk.Entry(self)
        self.ent_department.grid(row=5, column=1, rowspan=1)

        self.but_save = ttk.Button(self, text='Create table', command=self.create_table)
        self.but_save.grid(row=7, column=2, columnspan=1)

        self.but_close = ttk.Button(self, text='Close', command=self.quit)
        self.but_close.grid(row=7, column=0, columnspan=1)

    def create_table(self):
        pass

    def create_database(self):
        try:
            db = sqlite3.connect(self.entry.get())
            print("Creating database : " + self.entry.get())
        except Error as e:
            print(e)
        finally:
            db.close()




if __name__ == '__main__':
    app = App()
    app.mainloop()