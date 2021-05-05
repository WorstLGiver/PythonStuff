def formatnumber(num):
    if num % 1 == 0:
        return int(num)
    else:
        return num


while True:
    try:
        height = float(input("Height: "))
        side1 = float(input("Base 1: "))
        side2 = float(input("Base 2: "))
        unit = input("Unit: ")
        answer = side1 + side2
        answer = 1 / 2 * height * answer
        print("A = 1/2(h)(b1 + b2)")
        print("1/2" + "(" + str(formatnumber(height)) + ")(" + str(formatnumber(side1)), "+", str(formatnumber(side2)) + ")")
        print("A =", str(formatnumber(answer)) + unit)
    except Exception:
        print("Enter a number PogO")
