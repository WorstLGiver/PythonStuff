def formatnumber(num):
    if num % 1 == 0:
        return int(num)
    else:
        return num


while True:
    try:
        first = float(input("First Number: "))
        second = float(input("Second Number: "))
        answer = first / second
        print(formatnumber(first), "/", formatnumber(second), "=", formatnumber(answer))
    except Exception:
        print("Enter a number.")
