class Person(object):
    __name = None
    __id = None

    # def __init__(self, name, id):
    #     self.name = name
    #     self.id = id

    def SetName(self, name):
        self.__name = name

    def SetId(self, id):
        self.__id = id

    def GetName(self):
        return self.__name

    def GetId(self, id):
        return self.__id

class Student(Person):
    __classes = {}
    __avg = 0.0

    def SetKor(self, score):
        self.__classes["kor"] = score

    def SetMath(self, score):
        self.__classes["math"] = score

    def SetPython(self, score):
        self.__classes["python"] = score

    def SetAvg(self, avg):
        self.__avg = avg

    def GetKor(self):
        return self.__classes["kor"]

    def GetMath(self):
        return self.__classes["math"]

    def GetPython(self):
        return self.__classes["python"]

    def GetAvg(self):
        return self.__avg

students = []
avg = 0.0

for i in range(5):
    students.append(Student())
    students[i].SetName(input("이름: "))
    students[i].SetId(int(input("주민번호: ")))
    students[i].SetKor(int(input("국어 점수: ")))
    students[i].SetMath(int(input("수학 점수: ")))
    students[i].SetPython(int(input("파이썬 점수: ")))

    avg += students[i].GetPython()

avg /= len(students)

for student in students:
    print(avg)
    if(student.GetPython() >= avg):
        print(student.GetName())