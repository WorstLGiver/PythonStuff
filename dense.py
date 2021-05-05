while True:
    try:
        print("Chose one: \n(1) Density\n(2) Volume\n(3) Mass")
        choice = input("Chose 1, 2, or 3: ")
        if choice == "1":
            print("Enter the mass and volume.")
            mass = float(input("Mass: "))
            volume = float(input("Volume: "))
            answer = mass / volume
            print(str(mass) + "/" + str(volume), "=", answer)
        elif choice == "2":
            print("Enter the mass and density.")
            mass = float(input("Mass: "))
            density = float(input("Density: "))
            answer = mass / density
            print(str(mass) + "/" + str(density), "=", answer)
        elif choice == "3":
            print("Enter the density and volume")
            density = float(input("Density: "))
            volume = float(input("Volume: "))
            answer = density * volume
            print(density, "*", volume, "=", answer)
        else:
            print("Please pick one of the choices 1, 2, or 3.")
    except Exception:
        print("Please enter a number.")
