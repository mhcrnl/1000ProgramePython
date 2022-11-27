#!/usr/bin/env python3
import sqlite3

con = sqlite3.connect('mydatabase.db')
cursorObj = con.cursor()