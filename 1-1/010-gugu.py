for i in range(2, 6, 1):
    for j in range(1, 10, 1):
        print(str(i) + " * " + str(j) + " = " + str(i * j))

i = 2
while i<=5:
    j = 1
    while j<9:
        j += 1
        print(str(i) + " * " + str(j) + " = " + str(i * j))
    i += 1