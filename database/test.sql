-- 如果表已存在，先删除（方便反复测试）
DROP TABLE IF EXISTS students;

-- 学生表
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    gender TEXT CHECK (gender IN ('男', '女')),
    phone TEXT,
    class_name TEXT,
    major TEXT
);

-- 初始化测试数据
INSERT INTO students (student_id, name, gender, phone, class_name, major)
VALUES
('20244140001', '张三', '男', '13900000001', '24软件工程1班', '软件工程'),
('20244140002', '李四', '女', '13800000002', '24软件工程1班', '软件工程'),
('20244140003', '王五', '男', '13800000003', '24计算机科学1班', '计算机科学');
