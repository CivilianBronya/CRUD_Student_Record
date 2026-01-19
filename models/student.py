class Student:
    def __init__(
        self,
        student_id: str,
        name: str,
        gender: str,
        phone: str,
        class_name: str,
        major: str,
        id: int = None
    ):
        self.id = id
        self.student_id = student_id
        self.name = name
        self.gender = gender
        self.phone = phone
        self.class_name = class_name
        self.major = major

    def to_tuple(self):
        """
        转换为数据库可用的 tuple
        数据库对格式是刚性，没法直接喂给 SQLite
        """
        return (
            self.student_id,
            self.name,
            self.gender,
            self.phone,
            self.class_name,
            self.major
        )

    def to_log_dict(self):
        """
        用于日志的安全字段,不该和数据库绑死
        """
        return {
            "student_id": self.student_id,
            "name": self.name,
            "gender": self.gender,
            "class_name": self.class_name,
            "major": self.major
        }

    def to_log_str(self):
        """
        日志字符串形式
        """
        return (
            f"student_id={self.student_id}, "
            f"name={self.name}, "
            f"gender={self.gender}, "
            f"class={self.class_name}, "
            f"major={self.major}"
        )

    def __repr__(self):
        return (
            f"Student(student_id='{self.student_id}', "
            f"name='{self.name}', gender='{self.gender}', "
            f"phone='{self.phone}', class_name='{self.class_name}', "
            f"major='{self.major}')"
        )
