# 과일 명 가격 개수
# 배 2000 3
# 사과 1500 5
# 딸기 1800 2
# 참외 2300 5

# 5개 이하는 5개로
# 사야 할 과일과 그에 드는 각각의 비용과 총비용을

if __name__ == "__main__":
    fruits = {"fear": [2000, 3], "apple": [1500, 5], "strawberry": [1800, 2], "melon": [2300, 5]}

    requireFruits = {}
    requireMoney = 0

    sum = 0

    for fruit in fruits.items():
        if fruit[1][1] < 5:
            requireMoney = fruit[1][0] * fruit[1][1]
            print(fruit[0], "을 ", requireMoney, "원 구매해야합니다.")

            sum += requireMoney
        else:
            print(fruit[0], "은 구매할 필요가 없습니다")

    print("전체 금액:", sum, "원")