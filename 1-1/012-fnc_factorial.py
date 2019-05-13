# Prog: factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(int(input("임의의 양수 하나를 입력 하시오: "))))