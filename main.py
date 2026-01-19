from ui.menu import show_menu
from ui.student_ui import StudentUI

def main():
    ui = StudentUI()

    while True:
        show_menu()
        choice = input("请选择操作：").strip()

        if choice == "1":
            ui.add_student()
        elif choice == "2":
            ui.delete_student()
        elif choice == "3":
            ui.update_student()
        elif choice == "4":
            ui.show_student()
        elif choice == "0":
            print("退出系统, See you next time!")
            break
        else:
            print("无效选项，请重新输入")

if __name__ == "__main__":
    main()
