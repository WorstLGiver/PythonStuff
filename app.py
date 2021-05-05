import math
while True:
    try:
        print('Cube/Rectangular Prism(1) Cylinder(2)')
        shape = input('Shape(1/2): ')
        if shape in ('1', '2'):
            if shape == '1':
                print('Enter the Length, Width, and Height below')
                a = float(input("First number:"))
                b = float(input("Second Number: "))
                c = float(input('Third Number: '))
                unit = input("Unit: ")

                area = 2 * a * b + 2 * a * c + 2 * b * c

                volume = a * b * c

                print('2 *', a, '*', b, '+ 2 *', a, '*', c, '+ 2 *', b, '*', c)
                print(2 * a * b, '+', 2 * a * c, '+', 2 * b * c)
                print("Surface Area of Cuboid is: {0:.2f}".format(area), unit + '²')
                print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                print(a, '*', b, '*', c)
                print("Volume of Cuboid is: {0:.2f}".format(volume), unit + '³')

            elif shape == '2':
                print('Enter the Radius and Height below')
                a = float(input("Radius:"))
                b = float(input("Height: "))
                unit = input("Unit: ")

                area = 2 * 3.14 * a * b + 2 * 3.14 * a ** 2

                volume = a ** 2 * 3.14 * b

                print(2, '*', math.pi, '*', a, '*', b, '+', 2, '*', math.pi, '*', str(a) + '²')
                print(2 * math.pi * a * b, '+', 2 * math.pi * a ** 2)
                print("Surface Area of Cylinder is: {0:.2f}".format(area), unit + '²')
                print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                print(str(a) + '²', '*', math.pi, "*", b)
                print("Volume of Cylinder is: {0:.2f}".format(volume), unit + '³')
        else:
            print('Invalid Input')

    except Exception:
        print("You didn't enter a number or decimal number")
