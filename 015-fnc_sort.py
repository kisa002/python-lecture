def sortf(x, y, z):
    arr = []
    arr.append(x)
    arr.append(y)
    arr.append(z)

    for i in range(3):
        for j in range(i+1, 3):
            if arr[i] < arr[j]:
                arr[i] ^= arr[j]
                arr[j] ^= arr[i]
                arr[i] ^= arr[j]

    print(arr[0], arr[1], arr[2])

sortf(5, 2, 30)