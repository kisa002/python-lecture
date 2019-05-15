class Person(object):
    name = ""

    def __init__(self, name, id, age, height, weight):
        self.name = name
        self.id = id
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self):
        return self.name + "은 " + str(self.age) + "세이며 키는 " + str(self.height) + "cm, 몸무게는 " + str(self.weight) + "kg 이다."

personList = []
personList.append(Person("을지문덕", len(personList), 20, 170, 50))
personList.append(Person("계백", len(personList), 22, 173, 55))
personList.append(Person("김유신", len(personList), 24, 177, 53))
personList.append(Person("강감찬", len(personList), 26, 164, 46))
personList.append(Person("이순신", len(personList), 28, 199, 70))

for item in personList:
    print(item)