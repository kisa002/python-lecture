money = 100000
rate = 12
year = 24

result = money * (1 + rate / 100) ** year

print("원금 " + str(money) + "원의 " + str(year) + "년 후의 " + str(rate) + "% 이자의 상한 원리금은 " + str(result) + "원입니다")