import pymysql
import generator as gt
conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='123456',db='college',
charset='utf8')
course = conn.cursor()#创建游标
num=gt.creatnum()
for i in range(10):
    print(num[i])
sql="""select * from topacademic"""
course.execute(sql)#使用游标执行sql语句
results = course.fetchall()
for i in results:
    top=i[0]
    name = i[1]
    print("学校排名为%s,学校名称为%s" %(top, name))
conn.commit()#用数据库进行提交
course.close()
conn.close()