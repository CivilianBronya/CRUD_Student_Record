import re

def input_required(prompt: str) -> str:
    """
    必填输入：非空、非纯空格
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("该字段不能为空，请重新输入。")


def validate_phone(phone: str) -> bool:
    """
    国际手机号（简化版）
    支持：中国 / 日本 / 美国 / 英国
    """
    patterns = [
        r"^1[3-9]\d{9}$",            # 中国（国内）
        r"^\+86\d{11}$",             # 中国（国际）
        r"^0[7-9]0\d{8}$",            # 日本
        r"^\+81\d{9,10}$",            # 日本（国际）
        r"^\d{10}$",                  # 美国
        r"^\+1\d{10}$",               # 美国（国际）
        r"^07\d{9}$",                 # 英国
        r"^\+44\d{9,10}$"             # 英国（国际）
    ]
    return any(re.match(p, phone) for p in patterns)

def validate_student_id(student_id: str) -> bool:
    """
    学号校验 11 位数字
    """
    return student_id.isdigit() and len(student_id) == 11

MAJORS = [
    # 信息技术类
    "人工智能技术应用",
    "大数据技术",
    "信息安全技术应用",
    "软件技术",
    "计算机网络技术",
    "影视多媒体技术",
    "影视动画（数字动画方向）",

    # 智慧与数字化服务
    "智慧健康养老服务与管理",
    "商务数据分析与应用",
    "电子商务",
    "酒店管理与数字化运营",

    # 工程与制造
    "飞行器数字化制造技术（飞机制造技术方向）",
    "机电一体化技术",
    "汽车检测与维修技术",

    # 经济与管理
    "工商企业管理",
    "工商企业管理（中法合作）",
    "旅游管理",
    "会展策划与管理",

    # 外语与国际方向
    "应用英语",
    "应用日语（动漫运营方向）",
    "应用德语（国际商务方向）",
    "应用法语（商务法语方向）",

    # 教育与服务
    "学前教育",
    "婴幼儿托育服务与管理",
    "音乐教育",

    # 艺术与设计
    "广告艺术设计（新媒体艺术方向）",
    "环境艺术设计（室内设计方向）",
]

GENDERS = ["男", "女"]


def input_phone(prompt: str) -> str:
    """
    手机号输入
    """
    while True:
        phone = input(prompt).strip()
        if not phone:
            print("手机号不能为空")
            continue
        if validate_phone(phone):
            return phone
        print("手机号格式不正确（支持 CN / JP / US / UK）")

def input_student_id(prompt: str) -> str:
    while True:
        student_id = input_required(prompt)
        if validate_student_id(student_id):
            return student_id
        print("学号格式不正确（需为 11 位数字）")


def input_major(prompt: str) -> str:
    while True:
        print("可选专业：")
        for idx, major in enumerate(MAJORS, start=1):
            print(f"{idx}. {major}")

        choice = input_required(prompt)

        # 允许输入编号
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(MAJORS):
                return MAJORS[index]

        # 允许直接输入名称
        if choice in MAJORS:
            return choice

        print("请输入有效的专业编号或名称")


def input_gender(prompt: str) -> str:
    while True:
        print("可选性别：")
        for idx, gender in enumerate(GENDERS, start=1):
            print(f"{idx}. {gender}")

        choice = input_required(prompt)

        # 允许输入编号
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(GENDERS):
                return GENDERS[index]

        # 允许直接输入性别
        if choice in GENDERS:
            return choice

        print("请输入有效的性别编号或名称")