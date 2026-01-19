import sqlite3

class DBManager:
    def __init__(self, db_path="database/test.db"):
        self.db_path = db_path

    def execute(self, sql, params=(), fetch=False):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            cursor.execute(sql, params)
            conn.commit()
            if fetch:
                return cursor.fetchall()
        finally:
            conn.close()
