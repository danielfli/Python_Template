import sqlite3

# create a connection
conn = sqlite3.connect("students.db")


class DatabaseSQL:
    def __init__(self):
        self.conn = sqlite3.connect("students.db")
        self.cur = self.conn.cursor()
        # create a table
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY, name text, email text, course text, payment text)"
        )
        self.conn.commit()
