def print_baggage_items(*items, **item_with_count):
    print("-----단일 품목-----")
    for item in items:
        print(item)

    print("-----다중 품목-----")
    for count in item_with_count:
        print(count + " " + str(item_with_count[count]) + "개")

print_baggage_items("laptop", "camera", "charger", socks=8, pants=2, shirts=4)