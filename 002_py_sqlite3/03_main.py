#!/usr/bin/env python3

import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('mydatabase03.db')
        return con
    except Error:
        print(Error)

def sql_table(con):
    cursorObj =  con.cursor()
    cursorObj.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, departament text, position text, hireDate text)")
    con.commit()

con = sql_connection()
sql_table(con)