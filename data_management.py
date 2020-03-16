import sqlite3

class Data_base(object):
    def __init__(self, name):
        """ initialize a database """
        self.record_name = record_name
        self.connection = sqlite3.connect(f"{self.record_name}.db")
        self.cursor = self.connection.cursor()
        
    def create_table(self, name, properties):
        """
        create a table in your data base
        param:
            self
            name(str) -> table name
            properties(dict) -> properties that you want to set your column with ex: {firstName: text, lastName: text, pay: integer}
        """
        if type(name) == str and type(properties) == dict:
            self.cursor.execute("""CREATE TABLE :name( )""")
        else:
            raise TypeError("wrong data type passed in the function")
    
    def insert_data(self, table_name, values):
        pass

    def delete_data(self, table_name, values):
        pass

    def get_data(self, table_name, criteria):
        pass
    
    def 

