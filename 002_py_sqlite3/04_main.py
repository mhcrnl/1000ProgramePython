#!/usr/bin/env python3

import sqlite3

con = sqlite3.connect('mydatabase03.db')

def sql_insert(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO employees(id, name, salary, departament, position, hireDate) VALUES(?,?,?,?,?,?)', entities)
    con.commit()

entities = (1, 'Andrew', 800, 'IT', 'Tech', '2022-11-27')
sql_insert(con, entities)
