ls = list()

while True:
    name = input("강아지의 이름을 입력 하시오(종료 시에는 엔터키)")
    if(name != ""):
        ls.append(name)
    else:
        break

print(ls)