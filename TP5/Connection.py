import sqlite3

class Connection:
    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()

    # Create the Database
    def init(self):
        self.cursor.execute("drop table if exists commune")
        self.cursor.execute("drop table if exists departement")
        self.cursor.execute("drop table if exists region")
        self.cursor.execute("create table commune()")
        self.cursor.execute("create table departement()")
        self.cursor.execute("create table region()")