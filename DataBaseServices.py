import sqlite3


class DataBaseServices:
    def __init__(self):
        self.connection = sqlite3.connect("database.db")

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                usuario TEXT NOT NULL,
                contrasena TEXT NOT NULL
            )
            """
        )
        self.connection.commit()
        cursor.close()

    def execute_query(self, query, params=()):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            cursor.close()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def fetch_query(self, query, params=()):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            results = cursor.fetchall()
            columns = [description[0] for description in cursor.description]
            results = [dict(zip(columns, row)) for row in results]
            cursor.close()
            return results
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return None
        
    
    def fetch_one(self, query, params=()):
      try:
          cursor = self.connection.cursor()
          cursor.execute(query, params)
          result = cursor.fetchone()
          columns = [description[0] for description in cursor.description]
          if result:
              result = dict(zip(columns, result))
          cursor.close()
          return result
      except sqlite3.Error as e:
          print(f"An error occurred: {e}")
          return None
            
db_service = DataBaseServices()