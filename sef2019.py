phoneList = []
numOfData = 0


def InputData(name, number):
    phoneList.append({"name": name, "number": number})
    global numOfData
    numOfData += 1


def ShowData(data):
    print("-------------------")
    print("이름 :", data["name"])
    print("번호 :", data["number"])
    print("-------------------")


def SearchData(name):
    for item in phoneList:
        if item["name"] == name:
            print("이름:", item["name"])
            print("전화번호:", item["number"])
            return

    print("찾는 이름이 없습니다.")

# Input Your Code

def DeleteData(name):
    global numOfData

    for item in phoneList:
        if item["name"] == name:
            phoneList.remove(item)
            numOfData -= 1
            return

    print("찾는 이름이 없습니다.")

# Input Your Code

while True:
    print("============================")
    print("현재 데이터 개수 : {", numOfData, "}개")
    print("1. 전화번호 추가")
    print("2. 전화번호 검색")
    print("3. 전화번호 삭제")
    print("4. 전화번호 전체출력")
    print("5. 종료")
    print("============================")
    menu = int(input("선택 >> "))

    if menu == 1:
        name = input("이름 입력 : ")
        number = input("번호 입력 : ")
        InputData(name, number)

    elif menu == 2:
        search_name = input("검색할 이름 : ")
        SearchData(search_name)

    elif menu == 3:
        delete_name = input("삭제할 이름 : ")
        DeleteData(delete_name)

    elif menu == 4:
        for i in phoneList:
            ShowData(i)

    elif menu == 5:
        print("종료하겠습니다.")
    else:
        print("올바른 선택이 아닙니다.")
