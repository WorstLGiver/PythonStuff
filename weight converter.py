print('Chose one \n(1) Kg to Lbs \n(2) C to F \n(3) Cm to Inches')

while True:
    try:
        choice = input('Enter choice (1/2/3): ')
        if choice == '1':
            weight = float(input('Weight: '))
            system = input("(K)g or (L)bs: ")
            if system.lower() == 'l':
                conversion = weight / 2.205
                print("Weight in Kg:" + str(round(conversion, 1)))
            elif system.lower() == 'k':
                conversion = weight * 2.205
                print("Weight in Lbs:" + str(round(conversion, 1)))
            else:
                print("Chose one of the choices (K) or (L)")

        elif choice == '2':
            Temperature = float(input('Temperature: '))
            system = input("C or F: ")
            if system.lower() == 'c':
                conversion = Temperature * 9 / 5 + 32
                print("Temperature in F:" + str(round(conversion, 1)))
            elif system.lower() == 'f':
                conversion = Temperature - 32 * 5 / 9
                print("Temperature in C:" + str(round(conversion, 1)))
            else:
                print("Chose one of the choices (C) or (F)")

        elif choice == '3':
            length = float(input('Length: '))
            system = input("(C)m or (In)ches: ")
            if system.lower() == 'in':
                conversion = length * 2.54
                print("Length in Cm:" + str(round(conversion, 1)))
            elif system.lower() == 'c':
                conversion = length / 2.54
                print("Length in Inches:" + str(round(conversion, 1)))
            else:
                print("Chose one of the choices (C) or (In)")

        else:
            print('Incorrect choice')
    except Exception:
        print("Please enter a number by itself")
