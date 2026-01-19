# 学生管理系统（CRUD_Student_Record）

- 本项目是一个基于 Python + SQLite + 面向对象的学生管理系统，支持增删改查（CRUD）操作，并带有日志记录功能
- （本人的python大作业，本来没那么复杂）
- 有兴趣的可以下载玩玩，如果提交issue，也可能会后续更新
---


> 注意：`logs/` 文件夹和 SQLite 数据库文件不上传，需要自己部署，但初步的sql代码可直接使用


## 使用说明

1. 确保 Python 环境已安装，并安装依赖（如果有额外依赖可说明）。
2. 项目使用 SQLite，运行前需先创建数据库：
```bash
sqlite3 students.db < database/test.sql
```
运行主程序：

```bash
python main.py
```
---
## 系统将支持以下操作：

添加学生信息

删除学生信息

修改学生信息

显示学生信息（单人或多条查询）

日志记录（位于 logs/app.log）

---

## 注意事项

本项目仅供学习和演示用途，数据和代码可能不稳定。

SQLite 数据库文件需自行创建，不随项目上传。

日志文件 logs/app.log 不上传。

---
