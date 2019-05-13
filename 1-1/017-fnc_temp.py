def ShowMenu():
    print("--------------------")
    print("     [ 메뉴 선택 ]")
    print("[c] 섭씨온도에서 화씨온도로 변환")
    print("[f] 화씨온도에서 섭씨온도로 변환")
    print("[q] 종료")
    print("--------------------")
    n = input("메뉴를 선택해주세요: ")
    print("--------------------")
    SelectMenu(n)

def SelectMenu(n):
    if n == 'q':
        print("프로그램을 종료합니다.")
        return True

    print("     [ 온도 입력 ]")
    if n == 'c':
        print("섭씨 온도를 입력해주세요: ", end='')
    else:
        print("화씨 온도를 입력해주세요: ", end='')

    temp = input()
    print("--------------------")
    print("     [ 온도 변환 ]")

    if(n == 'c'):
        print("섭씨:", temp)
        print("화씨:", CtoF(temp))
    elif(n == 'f'):
        print("화씨:", temp)
        print("섭씨:", CtoF(temp))

    ShowMenu()

def CtoF(temp):
    return int(temp) * 1.8 + 32

def FtoC(temp):
    return (int(temp) - 32) / 1.8

if __name__ == "__main__":
    ShowMenu()