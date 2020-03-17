import sqlite3
import datetime

class Data_base(object):
    def __init__(self, name):
        """ initialize a database """
        self.record_name = name
        self.connection = sqlite3.connect(f"{self.record_name}.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS balance_sheet (id integer PRIMARY KEY NOT NULL AUTOINCREMENT
                                                                         user_name text
                                                                         expense integer
                                                                         revenue integer
                                                                         time text
                                                                        )""")
        sef.cursor.execute("""CREATE TABLE IF NOT EXISTS users (uid integer NOT NULL AUTO_INCREMENT
                                                  user_name text
                                                  pass_word_hash text
                                                  balance integer)""")
        self.connection.commit()


    def update_data(self, column_name, value):
        self.cursor.execute("UPDATE users SET ? = ?", (column_name, value))
        self.connection.commit()


    def insert_data(self, table_name, values):
        if table_name == "balance_sheet":
            self.cursor.execute("INSERT INTO balance_sheet VALUES (?, ?, ?, ?)", (user_name, values[0], values[1], str(datetime.datetime.today)))# todo: find a way to put user name in it
            self.connection.commit()

        elif table_name == "users":
            self.cursor.execute("INSERT INTO users VALUES (?, ?, ?)", (values[0], values[1], 0))
            self.connection.commit()

        else:
            raise ValueError("table name does not exist")

    def delete_data(self, value):
        self.cursor.execute("DELETE FROM balance_sheet WHERE id = ?", (value,))
        self.connection.commit()

    def get_data(self, table_name, criteria):
        pass
    

