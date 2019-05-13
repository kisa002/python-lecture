price = int(input("물건 값을 입력하세요: "))

value1000 = int(input("1000원 지폐 개수: ")) * 1000
value500 = int(input("500원 동전 개수: ")) * 500
value100 = int(input("100원 동전 개수: ")) * 100

sum = value1000 + value500 + value100

sum -= price

print("500원: " + str(sum // 500) + "개")
sum -= sum // 500 * 500
print("100원: " + str(sum // 100) + "개")
sum -= sum // 100 * 100
print("10원: " + str(sum // 10) + "개")
sum -= sum // 10 * 10
print("1원: " + str(sum // 1) + "개")
sum -= sum // 1 * 1