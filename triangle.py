import math


def formatnumber(num):
    if num % 1 == 0:
        return int(num)
    else:
        return num


while True:
    print("Find the missing side of a right triangle")
    sideone = float(input("Side 1: "))
    sidetwo = float(input("Side 2: "))
    unit = input("Unit: ")
    side = formatnumber(sidetwo ** 2 + sideone ** 2)
    sidethree = formatnumber(math.sqrt(side))
    print("a² + b² = c²")
    print(str(sideone) + "² +", str(sidetwo) + "² = c²")
    print(str(sideone) + "² +", str(sidetwo) + "² =", side)
    print("c = √" + str(side))
    print("c = " + str(sidethree))
    print("Side three of the triangle is " + str(sidethree) + unit)
