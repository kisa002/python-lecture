def multiplicationTable(dan):
    for i in range(dan, dan + 1):
        for j in range(1, 10):
            print(i, "*", j, "=", i*j)

dan = int(input())
multiplicationTable(dan)