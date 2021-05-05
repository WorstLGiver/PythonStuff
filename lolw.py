while True:
    first = input("First Number: ")
    second = input("Second Number: ")
    decimal = float(first) / float(second)
    decimal = decimal * 100
    a = 100
    while decimal % 1 != 0:
        decimal = decimal * 10
        a = a * 10
    decimal = str(decimal) + "/" + str(a)
    print(decimal)
