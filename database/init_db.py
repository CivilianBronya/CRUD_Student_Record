import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "test.db"
SQL_PATH = Path(__file__).parent / "test.sql"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    with open(SQL_PATH, "r", encoding="utf-8") as f:
        sql_script = f.read()

    cursor.executescript(sql_script)
    conn.commit()
    conn.close()

    print("数据库初始化完成")

if __name__ == "__main__":
    init_db()
