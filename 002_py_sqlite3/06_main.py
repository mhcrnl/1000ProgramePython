import sqlite3
import os

class Database:
    def open(self):
        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()
        print(self.conn)

    def close(self):
        self.conn.close()

    def table(self, name):
        "Create a table"
        self.c.execute(f'''CREATE TABLE {name}(
                     date text,
                     account text,
                     debit real,
                     credit real,
                     diff real
        )''')

    def add_row(self, tablename, data):
        " Insert a row of data"
        self.c.execute(f"INSERT INTO {tablename} VALUES {data}")

    def query(self, tablename, column=""):
        print(column)
        if column == "":
            for row in self.c.execute(f'SELECT * FROM {tablename}'):
                print(row)
        else:
            for row in self.c.execute(f'SELECT * FROM {tablename} ORDER BY {column}'):
                print(row)

    def commit(self):
        self.conn.commit()



app = Database()
app.open()

def create_table():
    app.table("journal")

def day_1():
    "2021.02.01"
    app.add_row("journal", ('2021-02-01','Cash',100,0,100))
    app.add_row("journal", ('2021-02-01','Cash',200,0,200))
    app.add_row("journal", ('2021-02-01','Cash',0,50,-50))
    app.commit()

# day_1()
app.query("journal", "diff")
app.close()


# os.startfile(".")