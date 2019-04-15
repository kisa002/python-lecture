def average_list(list):
    sum = 0

    for value in list:
        sum += value

    return sum / len(list)

list = [100, 60, 40]

avg = average_list(list)
print("Avg:", avg)