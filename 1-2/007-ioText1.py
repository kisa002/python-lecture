import os.path


if not os.path.isfile('text.txt'):
    print("text.txt 파일이 존재하지 않습니다")
else:
    with open('text.txt', 'r') as file:
        lines = file.readlines()

    with open('text.txt', 'w') as file:
        i = 1
        for line in lines:
            file.write(str(i) + ":" + line)
            i += 1