from services.student_service import StudentService
from models.student import Student
from utils.validator import *
import random
import string
class StudentUI:
    def __init__(self):
        self.service = StudentService()
    # 增
    def add_student(self):
        student = Student(
            student_id=input_student_id("学号："),
            name=input_required("姓名："),
            gender=input_required("性别："),
            phone=input_phone("手机号："),
            class_name=input_required("班级："),
            major=input_major("专业：")
        )
        created = self.service.create_student(student)
        print("新增成功：", created)
    # 改
    def update_student(self):
        print("\n修改学生信息")

        sid = input_student_id("请输入学号：")

        student = self.service.get_student_by("student_id", sid)
        if not student:
            print("未找到该学生")
            return

        print("当前学生信息：")
        print(student)

        while True:
            print("\n请选择要修改的字段：")
            print("1. 姓名")
            print("2. 性别")
            print("3. 手机号")
            print("4. 班级")
            print("5. 专业")
            print("0. 返回上一级")

            choice = input("请选择：").strip()

            if choice == "0":
                return

            field_map = {
                "1": ("name", input_required, "新姓名："),
                "2": ("gender", input_required, "新性别："),
                "3": ("phone", input_phone, "新手机号："),
                "4": ("class_name", input_required, "新班级："),
                "5": ("major", input_major, "新专业："),
            }

            if choice not in field_map:
                print("无效选择")
                continue

            field, input_func, prompt = field_map[choice]
            new_value = input_func(prompt)

            try:
                self.service.update_student_field(sid, field, new_value)
                print(f"修改成功：{field} 已更新")
            except Exception as e:
                print("修改失败：", e)
    # 查
    def show_student(self):
        print("\n查询学生信息")
        print("1. 按学号查询")
        print("2. 按姓名查询")
        print("3. 按手机号查询")
        print("4. 按班级查询")
        print("5. 按专业查询")
        print("6. 按性别查询")
        print("0. 返回")

        choice = input("请选择查询方式：").strip()

        if choice == "1":
            value = input_student_id("学号：")
            result = self.service.get_student_by("student_id", value)
            print("查询结果：", result)

        elif choice == "2":
            value = input_required("姓名：")
            result = self.service.get_student_by("name", value)
            print("查询结果：", result)

        elif choice == "3":
            value = input_phone("手机号：")
            result = self.service.get_student_by("phone", value)
            print("查询结果：", result)

        elif choice == "4":
            value = input_required("班级：")
            results = self.service.list_students_by("class_name", value)
            print(f"共查询到 {len(results)} 条记录：")
            for stu in results:
                print(stu)

        elif choice == "5":
            value = input_major("专业：")
            results = self.service.list_students_by("major", value)
            print(f"共查询到 {len(results)} 条记录：")
            for stu in results:
                print(stu)

        elif choice == "6":
            value = input_required("性别：")
            results = self.service.list_students_by("gender", value)
            print(f"共查询到 {len(results)} 条记录：")
            for stu in results:
                print(stu)

        elif choice == "0":
            return

        else:
            print("无效选择，请重新输入")
    # 删
    def delete_student(self):
        sid = input_student_id("请输入要删除的学号：")
        # 查询原学生信息
        student = self.service.get_student_by("student_id", sid)
        if not student:
            print("未找到该学生，无法删除")
            return

        print("将删除的学生信息：", student)

        # 生成验证码
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        print(f"真的要删除吗？会非常非常久，请在下方输入验证码以确认删除喵：{code}")
        confirm = input("验证码：").strip().upper()

        if confirm != code:
            print("验证码错误，删除已取消")
            return

        deleted = self.service.delete_student(sid)
        print(f"删除成功 学号={deleted}")


