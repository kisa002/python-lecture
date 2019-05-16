class Person(object):
    # def __init__(self, name, id):
    #     self.name = name
    #     self.id = id

    def SetName(self, name):
        self._name = name

    def SetId(self, id):
        self._id = id

    def GetName(self):
        return self._name

    def GetId(self, id):
        return self._id


class Student(Person):
    def __init__(self):
        self._classes = {}

    def SetKor(self, score):
        self._classes["kor"] = score

    def SetMath(self, score):
        self._classes["math"] = score

    def SetPython(self, score):
        self._classes["python"] = score

    def SetAvg(self, avg):
        self._avg = avg

    def GetKor(self):
        return self._classes["kor"]

    def GetMath(self):
        return self._classes["math"]

    def GetPython(self):
        return self._classes["python"]

    def GetAvg(self):
        return self._avg


students = []
avg = 0.0

for i in range(5):
    students.append(Student())

    if i == 0:
        print(" ⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽")

    students[i].SetName(input("|이름: "))
    students[i].SetId(int(input("|주민번호: ")))
    students[i].SetKor(int(input("|국어 점수: ")))
    students[i].SetMath(int(input("|수학 점수: ")))
    students[i].SetPython(int(input("|파이썬 점수: ")))
    students[i].SetAvg((students[i].GetKor() + students[i].GetMath() + students[i].GetPython()) / 3)
    print(" ⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽")

    avg += students[i].GetPython()

avg /= len(students)

for student in students:
    if student.GetPython() >= avg:
        print(student.GetName())
