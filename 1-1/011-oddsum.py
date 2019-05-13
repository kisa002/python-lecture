n = int(input())
sum = 0

limit = 17 * int(n/17)

for i in range(1, n+1):
    if i % 3 != 0:
        sum += i

    if i % limit == 0:
        break

print (sum)