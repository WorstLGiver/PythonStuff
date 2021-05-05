import random


def tid():
    a = str(random.randint(1, 999999999))
    hexcode = hex(int(a))
    hexcode = hexcode.replace('0x', '')
    hexcode = "00040000" + str(hexcode)
    print(hexcode)


print("1 to 999999999 possibilities")
while True:
    try:
        repeat = int(input('How many title ids to generate?:'))
        i = 1
        while i <= repeat:
            tid()
            i = i + 1
    except Exception:
        print("Please enter a whole number")
