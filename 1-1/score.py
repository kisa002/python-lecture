# import test

def main():
    print("def main():")

    listScore = list()
    sum = 0

    for i in range(6):
        score = int(input("Score: "))
        listScore.append(score)
        sum += score

    print("Average: " + str(sum / len(listScore)))

def Ang():
    ls = [90, 30, 75, 100, 85, 96]

    sum = 0
    sum += ls[0]
    sum += ls[1]
    sum += ls[2]
    sum += ls[3]
    sum += ls[4]
    sum += ls[5]

    print(sum / 6)

print(__name__)

if __name__ == "__main__":
    print("바로 실행하셨네요.\nmain()을 실행합니다.")
    main()
else:
    print("다른 곳에서 불러오셨네요.\n메인을 실행하지 않습니다.")