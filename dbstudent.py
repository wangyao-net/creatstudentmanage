import pymysql
import generator as gt

# 学生信息包括学生姓名，学号，性别，年龄，学院，专业，电话
conn = pymysql.connect(host='localhost', port=3306, user='root',
                       passwd='123456', db='studentmanage', charset='utf8')
for i in range(len(gt.creatnum())-1):
    name = gt.creatname()[i]
    num = gt.creatnum()[i]
    sex = gt.creatsex()[i]
    age = gt.creatage()[i]
    college = gt.creatcollge()[i]
    major = gt.creatmajor()[i]
    phone = gt.creatphone()[i]
    course = conn.cursor()  # 创建游标
    sql = """insert into student_manage(name, num, sex, age, college, major, phone)
    values(%s,%s,%s,%s,%s,%s,%s)"""
    values=(name,num,sex,age,college,major,phone)
    course.execute(sql,values)
    course.close()
conn.commit()  # 用数据库进行提交
print("数据提交完成")
conn.close()
