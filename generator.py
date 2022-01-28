# 导入库文件
import random
import student_name


# 学生信息包括学生姓名，学号，性别，年龄，学院，专业，电话
# 生成姓名
# 定义学生姓名生成函数
def creatname():
    # 创建空的列表存储学生的姓名
    managename = []
    for i in range(1000):
        managename.append(student_name.random_name())
    return managename


# 生成学号
def creatnum():
    # 创建空的列表存储生成的学生学号
    managenum = []
    for i in range(1, 1000):
        managenum.append("2019102060" + str(i).zfill(3))
    return managenum


# 生成性别
def creatsex():
    # 创建空列表存储生成的学生性别
    a = ["男", "女"]
    managesex = []
    for i in range(1000):
        managesex.append(random.choice(a))
    return managesex


# 生成年龄
def creatage():
    # 创建空的列表存储生成的学生的年龄
    manageage = []
    for i in range(1000):
        manageage.append(random.randint(18, 15))
    return manageage


# 生成学院
def creatcollge():
    b = ["计算机学院", "数字媒体与创意设计学院", "电影与电视学院",
         "播映主持学院", "音乐学院", "软件工程学院", "机械自动化学院"]  # 需要其他学院自行添加
    # 创建空的列表存储生成的学生的学院信息
    managecollge = []
    for i in range(1000):
        managecollge.append(random.choice(b))
    return managecollge


# 生成专业
def creatmajor():
    c = ["", "", "", "", "", "", "", "", "", "", "", "", ""]  # 专业名称自行添加
    # 创建空列表存储学生的专业
    managemajor = []
    for i in range(1000):
        managemajor.append(random.choice(c))
    return managemajor


# 生成电话
def creatphone():
    managephone = []
    for i in range(1000):
        managephone.append(
            "1" + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(
                random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(
                random.randint(0, 9)) +
            str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(
                random.randint(0, 9)))
    return managephone


# 生成学生邮箱，此为备用选项，可加可删

# 定义main函数
def main():
    creatname()
    creatnum()
    creatsex()
    creatage()
    creatcollge()
    creatmajor()
    creatphone()


if __name__ == '__main__':
    main()
#cesium