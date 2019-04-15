def main():
    price = int(input("구입 금액을 입력하시오: "))

    if(price >= 100000):
        discount = price * 0.05
        print(discount, "원 할인 받아", price - discount, "원을 지불하셨습니다.")
    else:
        require = 100000 - price
        print(require, "원 더 구입하시면 5% 할인받으실 수 있습니다")

if __name__ == "__main__":
    main()