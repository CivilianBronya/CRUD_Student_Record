from database.student_dao import StudentDAO
from models.student import Student
from utils.logger import log_action

ALLOWED_SINGLE_FIELDS = {
    "student_id",
    "name",
    "phone"
}

ALLOWED_MULTI_FIELDS = {
    "class_name",
    "major",
    "gender"
}

ALLOWED_QUERY_FIELDS = {
    "student_id",
    "name",
    "phone"
}

ALLOWED_UPDATE_FIELDS = {
    "name",
    "phone",
    "gender",
    "class_name",
    "major"
}

class StudentService:
    def __init__(self):
        self.dao = StudentDAO()

    def create_student(self, student):
        self.dao.insert(student)
        log_action(
            "ACTION=INSERT "
            "MODULE=student_service.create_student "
            f"DATA={student}"
        )
        return student
    """
    修改字段对于学生ID这种无论如何什么理由都是固定的字段不写ALLOWED_UPDATE_FIELDS里
    而其他字段按照基本现实情况制作
    """

    def update_student_field(self, student_id, field, new_value):
        if field not in ALLOWED_UPDATE_FIELDS:
            raise ValueError(f"不允许修改的字段: {field}")

        # 查询原始数据
        result = self.dao.select_one_by_field("student_id", student_id)
        if not result:
            raise ValueError("学生不存在")

        # 临时封装成 Student 对象，单用select_one_by_field返回的是list of tuple但实际是列表
        row = result[0]
        student = Student(
            id=row[0],
            student_id=row[1],
            name=row[2],
            gender=row[3],
            phone=row[4],
            class_name=row[5],
            major=row[6]
        )

        old_value = getattr(student, field)
        if old_value == new_value:
            return False

        # 执行数据库更新
        self.dao.update_field(student_id, field, new_value)

        setattr(student, field, new_value)

        log_action(
            "ACTION=UPDATE "
            "MODULE=student_service.update_student_field "
            f"TARGET=student_id={student_id} "
            f"FIELD={field} "
            f"OLD_VALUE={old_value} "
            f"NEW_VALUE={new_value} "
            f"DATA={student}"
        )

        return student

    """
    制作的单人与多人需要分开字段，防止sql的数据注入错误问题，所以有了ALLOWED_XXX_FIELDS
    """
    # 单人查询
    def get_student_by(self, field, value):
        if field not in ALLOWED_SINGLE_FIELDS:
            raise ValueError(f"不支持的单人查询字段: {field}")

        result = self.dao.select_one_by_field(field, value)
        log_action(
            "ACTION=SELECT_ONE "
            "MODULE=student_service.get_student_by "
            f"CONDITION={field}={value} "
            f"DATA={result}"
        )
        return result

    # 多人查询
    def list_students_by(self, field, value):
        if field not in ALLOWED_MULTI_FIELDS:
            raise ValueError(f"不支持的多人查询字段: {field}")

        results = self.dao.select_many_by_field(field, value)
        log_action(
            "ACTION=SELECT_LIST "
            "MODULE=student_service.list_students_by "
            f"CONDITION={field}={value} "
            f"COUNT={len(results)}"
        )
        return results
    """
    实际作业不需要这么复杂，由于实际使用，在log里显示完整字段，要删除前先查完整信息
    """
    def delete_student(self, student_id):
        student = self.dao.select_one_by_field("student_id", student_id)
        if not student:
            log_action(
                "ACTION=DELETE "
                "MODULE=student_service.delete_student "
                f"TARGET=student_id={student_id} "
                "RESULT=NOT_FOUND"
            )
            return None

        self.dao.delete(student_id)

        log_action(
            "ACTION=DELETE "
            "MODULE=student_service.delete_student "
            f"DATA={student}"
        )

        return student
