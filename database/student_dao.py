from database.db_manager import DBManager

class StudentDAO:
    def __init__(self):
        self.db = DBManager()

    def insert(self, student):
        sql = """
        INSERT INTO students (student_id, name, gender, phone, class_name, major)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        self.db.execute(sql, student.to_tuple())

    def update_field(self, student_id, field, value):
        sql = f"UPDATE students SET {field} = ? WHERE student_id = ?"
        self.db.execute(sql, (value, student_id))

    def delete(self, student_id):
        sql = "DELETE FROM students WHERE student_id = ?"
        self.db.execute(sql, (student_id,))

    # 单人查询
    def select_one_by_field(self, field, value):
        sql = f"SELECT * FROM students WHERE {field} = ?"
        return self.db.execute(sql, (value,), fetch=True)

    # 多人查询
    def select_many_by_field(self, field, value):
        sql = f"SELECT * FROM students WHERE {field} = ?"
        return self.db.execute(sql, (value,), fetch=True)
