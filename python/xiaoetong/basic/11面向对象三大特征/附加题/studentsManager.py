import json
from student import Student

class StudentManagerSystem(object):
    # 定义一个学生列表
    def __init__(self) -> None:
        self.studentsList = []
    
    # def 

    def initilizer(self, savedir):
        # 从json文件中读取学生信息
        try:
            with open("studentsData.json", "r") as f:
                savedir = json.load(f)
                print(savedir)
        except FileNotFoundError:
            pass

        for key in savedir:
            student = Student(key, savedir[key][0], savedir[key][1])
            self.studentsList.append(student)


    def getNameKey(self, stud):
        """定义一个接口"""
        return stud.getName()

    def start(self):
        # 每一次执行循环需要输出的信息
        print("V1.0")
        print("1.添加学员信息")
        print("2.删除学员信息")
        print("3.修改学员信息")
        print("4.查询学员信息")
        print("5.遍历所有学员信息")
        print("6.保存学员信息")
        print("7.退出系统")
        print("——————————————————————————")

    def addInfo(self):
        """添加学生信息"""
        nameInput = input("请输入姓名：")
        ageInput = input("请输入年龄：")
        phoneInput = input("请输入电话号码：")
        newStd = Student(nameInput, ageInput, phoneInput)
        self.studentsList.append(newStd)

    def delInfo(self):
        """删除学生信息"""
        delName = input("请输入你要删除的学生名：")
        for student in self.studentsList:
            if self.getNameKey(student) == delName:
                self.studentsList.remove()
                print("学生已删除")
                break
        else:
            print("学生不存在")
        
    def changeInfo(self):
        """修改学生信息"""
        changeName = input("请输入你要修改的学生名：")
        for student in self.studentsList:
            if self.getNameKey(student) == changeName:
                student.changeName(input("请输入修改后的姓名："))
                student.changeAge(input("请输入修改后的年龄："))
                student.changePhone(input("请输入修改后的电话号码："))
                print("学生信息已修改，修改后信息如下（依次为姓名，年龄，电话号码）：" + student.name + student.age + student.phone)
                break
        
    def checkInfo(self):
        """查询学生信息"""
        checkName = input("请输入你要查询的学生名：")
        for student in self.studentsList:
            student = self.studentsList[student]
            if self.getNameKey(student) == checkName:
                print("以下是查询结果（依次为姓名，年龄，和电话）")
                print(student.name, student.age, student.phone)
                break
    
    def goThrough(self):
        """遍历学生列表"""
        for student in self.studentsList:
            print(student.name, student.age, student.phone)

    def saveInfo(self):
        """文件保存"""
        # 格式：json {name1: [age, phone], name2......}
        for student in self.studentsList:
            saveDir[student.name] = [student.age, student.phone]
        with open('studentsData.json', 'w') as f:
            json.dump(saveDir, f)
        print("保存完毕")

    def exitSystem(self):
        """退出系统"""
        print("感谢你使用通讯录管理系统V1.0，欢迎下次使用！")
        exit() # 因为在这里就break了，所以后面没有横线（）

    def operate(self):
        operationCode = input("请输入操作码：")

        if operationCode == "1":
            self.addInfo()
        elif operationCode == "2":
            self.delInfo()
        elif operationCode == "3":
            self.changeInfo()
        elif operationCode == "4":
            self.checkInfo()
        elif operationCode == "5":
            self.goThrough()
        elif operationCode == "6":
            self.saveInfo()
        elif operationCode == "7":
            self.exitSystem()
        else:
            print("Bad input, please retry agian. Notice the input shuold be numbers \"1-7\"")

    def end():
        input("按Enter以继续操作")
        print("——————————————————————————")


    # def run():
        